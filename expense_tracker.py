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

    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category (Food, Travel, etc.): ").strip()
    description = input("Enter description: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    if not date or not category or not description:
        print("Date, category, and description cannot be empty.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded yet.")
        return

    for expense in expenses:
        print(
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Description: {expense['Description']} | "
            f"Amount: {float(expense['Amount']):.2f}"
        )


# Filter expenses by category
def filter_expenses():
    category = input("Enter category to search: ").strip().lower()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = [
            expense for expense in reader
            if expense["Category"].lower() == category
        ]

    if not expenses:
        print("No expenses found for this category.")
        return

    print(f"\nExpenses in category: {category.title()}")

    for expense in expenses:
        print(
            f"{expense['Date']} | {expense['Description']} | "
            f"{float(expense['Amount']):.2f}"
        )


# Summarize expenses by category
def category_summary():
    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            totals[category] = totals.get(category, 0) + amount

    print("\n--- Category Summary ---")

    if not totals:
        print("No expenses recorded yet.")
        return

    for category, total in totals.items():
        print(f"{category}: {total:.2f}")

    print(f"Total spending: {sum(totals.values()):.2f}")


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()