import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDS = ["Date", "Category", "Description", "Amount"]


def initialize_file():
    """Create the CSV file with a header if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)


def load_expenses():
    """Read all saved expenses from the CSV file."""
    initialize_file()
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_expense():
    print("\n--- Add Expense ---")

    while True:
        date_text = input("Enter date (DD-MM-YYYY), or press Enter for today: ").strip()
        if not date_text:
            date_text = datetime.now().strftime("%d-%m-%Y")
            break
        try:
            datetime.strptime(date_text, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date. Please use DD-MM-YYYY.")

    while True:
        category = input("Enter category (e.g., Food, Travel, Shopping): ").strip()
        if category:
            break
        print("Category cannot be empty.")

    description = input("Enter description: ").strip()
    if not description:
        description = "-"

    while True:
        try:
            amount = float(input("Enter amount (₹): ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date_text, category.title(), description, f"{amount:.2f}"])

    print("Expense saved successfully.")


def view_expenses(expenses=None):
    """Display all expenses, or a supplied filtered list."""
    if expenses is None:
        expenses = load_expenses()

    print("\n--- Expenses ---")
    if not expenses:
        print("No expenses found.")
        return

    print("-" * 78)
    print(f"{'Date':<13} {'Category':<15} {'Description':<28} {'Amount (₹)':>12}")
    print("-" * 78)
    for item in expenses:
        try:
            amount = float(item["Amount"])
        except (ValueError, KeyError):
            amount = 0.0
        print(
            f"{item.get('Date', ''):<13} "
            f"{item.get('Category', '')[:15]:<15} "
            f"{item.get('Description', '')[:28]:<28} "
            f"{amount:>12.2f}"
        )
    print("-" * 78)


def search_by_category():
    category = input("Enter category to search: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    matches = [
        item for item in load_expenses()
        if item.get("Category", "").strip().casefold() == category.casefold()
    ]
    if matches:
        print(f"\nFound {len(matches)} expense(s) in category '{category}'.")
        view_expenses(matches)
    else:
        print(f"No expenses found for category '{category}'.")


def category_totals():
    totals = {}
    for item in load_expenses():
        category = item.get("Category", "").strip() or "Uncategorized"
        try:
            amount = float(item.get("Amount", 0))
        except ValueError:
            continue
        totals[category] = totals.get(category, 0.0) + amount

    print("\n--- Total Spent per Category ---")
    if not totals:
        print("No expenses found.")
        return

    for category, total in sorted(totals.items(), key=lambda pair: pair[0].casefold()):
        print(f"{category:<20} ₹{total:.2f}")
    print("-" * 32)
    print(f"{'Grand Total':<20} ₹{sum(totals.values()):.2f}")


def monthly_total():
    month_input = input("Enter month and year (MM-YYYY), e.g., 09-2026: ").strip()
    try:
        selected_month = datetime.strptime(month_input, "%m-%Y")
    except ValueError:
        print("Invalid month. Please use MM-YYYY, for example 09-2026.")
        return

    total = 0.0
    matches = []
    for item in load_expenses():
        try:
            expense_date = datetime.strptime(item.get("Date", ""), "%d-%m-%Y")
            amount = float(item.get("Amount", 0))
        except ValueError:
            continue
        if expense_date.year == selected_month.year and expense_date.month == selected_month.month:
            total += amount
            matches.append(item)

    print(f"\nTotal spending for {selected_month.strftime('%B %Y')}: ₹{total:.2f}")
    if matches:
        print(f"Number of expenses: {len(matches)}")
        view_expenses(matches)
    else:
        print("No expenses recorded for that month.")


def main():
    initialize_file()

    while True:
        print("\n" + "=" * 34)
        print("       EXPENSE TRACKER 2.0")
        print("=" * 34)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Category")
        print("4. Calculate Total per Category")
        print("5. Calculate Monthly Spending")
        print("6. Exit")
        print("=" * 34)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            category_totals()
        elif choice == "5":
            monthly_total()
        elif choice == "6":
            print("Thank you for using Expense Tracker 2.0!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
