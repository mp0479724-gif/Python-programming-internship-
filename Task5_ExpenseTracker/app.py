#!/usr/bin/env python3
"""Task 5: Command-line Expense Tracker using SQLite, argparse, and logging."""

import argparse
import csv
import logging
import math
import sqlite3
import sys
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "expenses.db"
LOG_FILE = BASE_DIR / "app.log"


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
        force=True,
    )


def connect_db():
    """Open the SQLite database and ensure the expenses table exists."""
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0)
        )
    """)
    connection.commit()
    return connection


def validate_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Date must use YYYY-MM-DD format.") from exc


def validate_amount(value):
    try:
        amount = float(value)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("Amount must be a valid number.") from exc
    if not math.isfinite(amount) or amount <= 0:
        raise argparse.ArgumentTypeError("Amount must be greater than zero.")
    return amount


def add_expense(args):
    category = args.category.strip().title()
    description = args.description.strip()
    if not category:
        raise ValueError("Category cannot be empty.")
    if not description:
        raise ValueError("Description cannot be empty.")
    with connect_db() as db:
        cursor = db.execute(
            "INSERT INTO expenses (expense_date, category, description, amount) VALUES (?, ?, ?, ?)",
            (args.date, category, description, args.amount),
        )
        expense_id = cursor.lastrowid
    logging.info("ADD id=%s category=%s amount=%.2f", expense_id, category, args.amount)
    print(f"Expense added successfully. ID: {expense_id}")


def list_expenses(_args):
    with connect_db() as db:
        rows = db.execute(
            "SELECT id, expense_date, category, description, amount FROM expenses ORDER BY expense_date, id"
        ).fetchall()
    logging.info("LIST count=%s", len(rows))
    if not rows:
        print("No expenses found.")
        return
    print(f"{'ID':<5} {'DATE':<12} {'CATEGORY':<16} {'DESCRIPTION':<25} {'AMOUNT':>10}")
    print("-" * 73)
    for row in rows:
        print(f"{row['id']:<5} {row['expense_date']:<12} {row['category']:<16} "
              f"{row['description'][:24]:<25} {row['amount']:>10.2f}")
    print(f"\nTotal records: {len(rows)}")


def report_expenses(args):
    with connect_db() as db:
        if args.month:
            monthly = db.execute(
                "SELECT substr(expense_date, 1, 7) AS period, SUM(amount) AS total "
                "FROM expenses WHERE substr(expense_date, 1, 7)=? GROUP BY period",
                (args.month,),
            ).fetchall()
        else:
            monthly = db.execute(
                "SELECT substr(expense_date, 1, 7) AS period, SUM(amount) AS total "
                "FROM expenses GROUP BY period ORDER BY period"
            ).fetchall()
        categories = db.execute(
            "SELECT category, SUM(amount) AS total FROM expenses "
            + ("WHERE substr(expense_date, 1, 7)=? " if args.month else "")
            + "GROUP BY category ORDER BY total DESC",
            ((args.month,) if args.month else ()),
        ).fetchall()
        grand = db.execute(
            "SELECT COALESCE(SUM(amount), 0) FROM expenses "
            + ("WHERE substr(expense_date, 1, 7)=?" if args.month else ""),
            ((args.month,) if args.month else ()),
        ).fetchone()[0]

    logging.info("REPORT month=%s total=%.2f", args.month or "all", grand)
    print("EXPENSE SUMMARY" + (f" - {args.month}" if args.month else " - ALL MONTHS"))
    print("\nMonthly totals:")
    if monthly:
        for row in monthly:
            print(f"  {row['period']}: {row['total']:.2f}")
    else:
        print("  No data available.")
    print("\nCategory totals:")
    if categories:
        for row in categories:
            print(f"  {row['category']}: {row['total']:.2f}")
    else:
        print("  No data available.")
    print(f"\nGrand total: {grand:.2f}")


def delete_expense(args):
    with connect_db() as db:
        cursor = db.execute("DELETE FROM expenses WHERE id = ?", (args.id,))
        deleted = cursor.rowcount
    if deleted:
        logging.info("DELETE id=%s", args.id)
        print(f"Expense with ID {args.id} deleted successfully.")
    else:
        logging.info("DELETE_NOT_FOUND id=%s", args.id)
        print(f"No expense found with ID {args.id}.")


def export_expenses(args):
    with connect_db() as db:
        if args.month:
            rows = db.execute(
                "SELECT expense_date, category, description, amount FROM expenses "
                "WHERE substr(expense_date, 1, 7)=? ORDER BY expense_date, id",
                (args.month,),
            ).fetchall()
        else:
            rows = db.execute(
                "SELECT expense_date, category, description, amount FROM expenses ORDER BY expense_date, id"
            ).fetchall()
    writer = csv.writer(sys.stdout)
    writer.writerow(["Date", "Category", "Description", "Amount"])
    for row in rows:
        writer.writerow([row["expense_date"], row["category"], row["description"], f"{row['amount']:.2f}"])
    logging.info("EXPORT month=%s count=%s", args.month or "all", len(rows))


def build_parser():
    parser = argparse.ArgumentParser(
        description="Track expenses using SQLite. Run 'python app.py <command> --help' for command details."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add = subparsers.add_parser("add", help="Add a new expense")
    add.add_argument("--date", type=validate_date, default=date.today().isoformat(),
                     help="Expense date in YYYY-MM-DD format (default: today)")
    add.add_argument("--category", required=True, help="Expense category")
    add.add_argument("--description", required=True, help="Short description")
    add.add_argument("--amount", required=True, type=validate_amount, help="Positive amount")
    add.set_defaults(func=add_expense)

    listing = subparsers.add_parser("list", help="List all expenses")
    listing.set_defaults(func=list_expenses)

    report = subparsers.add_parser("report", help="Show monthly and category summaries")
    report.add_argument("--month", help="Filter report by month, e.g. 2026-11")
    report.set_defaults(func=report_expenses)

    delete = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete.add_argument("--id", required=True, type=int, help="Expense ID")
    delete.set_defaults(func=delete_expense)

    export = subparsers.add_parser("export", help="Export expenses as CSV")
    export.add_argument("--month", help="Optional month filter, e.g. 2026-11")
    export.set_defaults(func=export_expenses)
    return parser


def main():
    setup_logging()
    parser = build_parser()
    args = parser.parse_args()
    try:
        if getattr(args, "month", None):
            try:
                datetime.strptime(args.month, "%Y-%m")
            except ValueError:
                parser.error("--month must use YYYY-MM format.")
        args.func(args)
    except (sqlite3.Error, OSError, ValueError) as exc:
        logging.exception("ERROR while running command=%s", args.command)
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        logging.exception("Unexpected error while running command=%s", args.command)
        print(f"An unexpected error occurred: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
