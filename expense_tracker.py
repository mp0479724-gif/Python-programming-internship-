import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add a new expense
def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# Display all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader, None)  # Skip header

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        print("-" * 75)
        print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>15}")
        print("-" * 75)

        for expense in expenses:
            date, category, description, amount = expense

            print(
                f"{date:<15}"
                f"{category:<15}"
                f"{description:<25}"
                f"₹{float(amount):>13.2f}"
            )

        print("-" * 75)


# Calculate total expenses
def calculate_total():
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Amount Spent: ₹{total:.2f}")


# Display expenses by category
def category_total():
    category_name = input("\nEnter category to calculate total: ")

    total = 0
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category_name.lower():
                total += float(row["Amount"])
                found = True

    if found:
        print(f"Total spent on {category_name}: ₹{total:.2f}")
    else:
        print("No expenses found for this category.")


# Main menu
def main():
    initialize_file()

    while True:
        print("\n================================")
        print("       EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Calculate Category Total")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_total()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


# Start the program
if __name__ == "__main__":
    main()