# Task 5 – Expense Tracker using SQLite

## Project overview
This command-line expense tracker upgrades the Task 4 CSV project to an SQLite database. It uses Python's built-in `sqlite3`, `argparse`, and `logging` modules to store expenses, run reports, and record application activity.

## Features
- Store expense records in `expenses.db` (SQLite).
- Add, list, and delete expenses using command-line subcommands.
- Generate monthly totals and category-wise totals.
- Validate dates and positive numeric amounts.
- Normalize category names to title case (for example, `food` becomes `Food`).
- Record actions and unexpected errors with timestamps in `app.log`.
- Optional CSV export.

## Requirements
- Python 3.8 or later (no third-party packages required).
- VS Code or another Python editor is optional.

## Installation and setup
1. Download or clone this repository.
2. Open a terminal in the `Task5_ExpenseTracker` folder.
3. Check Python: `python --version` (on some systems use `python3 --version`).
4. Run any command below. The application automatically creates `expenses.db` and the `expenses` table, and creates `app.log`.

## Usage and example commands

### Add an expense
```bash
python app.py add --date 2026-11-01 --category food --description Lunch --amount 150
```
Expected output:
```text
Expense added successfully. ID: 1
```

### Add another expense
```bash
python app.py add --date 2026-11-02 --category Travel --description Bus fare --amount 40
```

### List expenses
```bash
python app.py list
```
Example output:
```text
ID    DATE         CATEGORY         DESCRIPTION                   AMOUNT
-------------------------------------------------------------------------
1     2026-11-01   Food             Lunch                         150.00
2     2026-11-02   Travel           Bus fare                       40.00

Total records: 2
```

### Generate a report
```bash
python app.py report
```
Example output:
```text
EXPENSE SUMMARY - ALL MONTHS

Monthly totals:
  2026-11: 190.00

Category totals:
  Food: 150.00
  Travel: 40.00

Grand total: 190.00
```

To report only one month:
```bash
python app.py report --month 2026-11
```

### Delete an expense
Use the ID displayed by the `list` command:
```bash
python app.py delete --id 2
```
Expected output:
```text
Expense with ID 2 deleted successfully.
```

### Export to CSV (optional)
```bash
python app.py export --month 2026-11 > report.csv
```

## Files generated
- `app.py` – main Python CLI application.
- `expenses.db` – SQLite database created automatically when the app runs.
- `app.log` – timestamped application activity and error log.
- `terminal_captures/` – sample terminal captures for add, list, report, and delete.

## Validation
- Amount must be numeric, finite, and greater than zero.
- Date must be in `YYYY-MM-DD` format.
- Category and description cannot be empty.
- Category is saved in title case.
- Friendly error messages are displayed for invalid input.

## Database structure
The `expenses` table contains:
| Column | Description |
|---|---|
| `id` | Unique auto-incremented record ID |
| `expense_date` | Expense date (`YYYY-MM-DD`) |
| `category` | Normalized expense category |
| `description` | Expense description |
| `amount` | Positive numeric amount |

## Learning outcomes
- Working with SQLite databases in Python.
- Creating CLI commands using `argparse`.
- Writing SQL queries for totals and reports.
- Handling invalid input and database errors.
- Logging application activity for debugging.

## Author
Name: Your Name  
Internship: Python Programming Internship – Task 5
