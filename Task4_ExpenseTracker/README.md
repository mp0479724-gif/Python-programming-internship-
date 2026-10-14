# Python Programming Internship – Task 4
## Menu-Driven Expense Tracker (CSV)

A Python console application for recording and managing personal expenses. It stores expense records in a CSV file and provides options to view, search, and summarize spending.

## Features

- Add an expense with a date, category, description, and amount.
- Use today's date automatically when the date field is left blank.
- Save expense records in `expenses.csv`.
- View all saved expenses.
- Search expenses by category.
- Calculate total spending for a selected month and year.
- Calculate spending totals for each category and a grand total.
- Validate dates and amounts.
- Handle common file-reading and file-writing errors.

## Requirements

- Python 3.x
- Visual Studio Code or another Python editor (optional)

The program uses Python's built-in `csv`, `os`, `math`, and `datetime` modules. No third-party packages are required.

## Project Files

```text
Task4_ExpenseTracker/
├── expense_tracker.py
├── expenses.csv          # Created automatically when the program runs
└── README.md
```

## How to Run

1. Install Python 3.x if it is not already installed.
2. Save the program code as `expense_tracker.py`.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python expense_tracker.py
   ```

   On some systems, use `python3 expense_tracker.py` instead.

5. Choose an option from the menu and follow the prompts.

## Menu Options

| Option | Action |
| --- | --- |
| 1 | Add Expense |
| 2 | View All Expenses |
| 3 | Search Expenses by Category |
| 4 | Calculate Monthly Spending |
| 5 | Calculate Total per Category |
| 6 | Exit |

## Adding an Expense

When prompted, enter:

- **Date:** Use `DD-MM-YYYY`, or press Enter to use today's date.
- **Category:** For example, `Food`, `Travel`, or `Shopping`.
- **Description:** A short note about the expense. If left blank, `-` is saved.
- **Amount:** Enter a positive number in rupees.

The application creates `expenses.csv` automatically if it does not exist. Keep this file if you want to retain your saved records.

## CSV Format

The CSV file contains these columns:

```csv
Date,Category,Description,Amount
10-10-2026,Food,Lunch,150.00
10-10-2026,Travel,Bus fare,40.00
```

The rows above are examples only. Your file will contain the expenses you enter.

## Example

```text
====================================
        EXPENSE TRACKER
====================================
1. Add Expense
2. View All Expenses
3. Search Expenses by Category
4. Calculate Monthly Spending
5. Calculate Total per Category
6. Exit
====================================
Enter your choice (1-6): 1

--- Add Expense ---
Enter date (DD-MM-YYYY), or press Enter for today: 10-10-2026
Enter category (e.g., Food, Travel, Shopping): Food
Enter description: Lunch
Enter amount (₹): 150
Expense saved successfully.
```

This is illustrative sample output; actual results depend on the inputs entered.

## Learning Outcomes

This task provides practice with:

- Python functions and loops.
- Conditional statements and menu-driven programs.
- File handling and CSV reading/writing.
- Date validation with `datetime`.
- Input validation and exception handling.
- Filtering records and calculating totals.

## Limitations

- This is a console-based application and does not have a graphical user interface.
- Data is stored locally in a CSV file.
- There are no user accounts or cloud synchronization.

## Author

Add your name and internship details here before publishing the project.

## License

This project is intended for learning and internship practice. Add a license if you plan to distribute it publicly.
