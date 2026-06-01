import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):

    try:
        amount = float(input("Enter Amount: ₹"))
    except ValueError:
        print("Invalid Amount!")
        return

    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense Added Successfully!")


def view_expenses(expenses):

    if not expenses:
        print("No Expenses Found!")
        return

    print("\n===== EXPENSE LIST =====")

    for i, expense in enumerate(expenses, start=1):

        print("\nExpense #", i)
        print("Amount      : ₹", expense["amount"])
        print("Category    :", expense["category"])
        print("Description :", expense["description"])


def total_expenses(expenses):

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total}")


def category_report(expenses):

    report = {}

    for expense in expenses:

        category = expense["category"]

        if category in report:
            report[category] += expense["amount"]
        else:
            report[category] = expense["amount"]

    print("\n===== CATEGORY REPORT =====")

    for category, amount in report.items():
        print(category, ":", "₹", amount)


def delete_expense(expenses):

    view_expenses(expenses)

    try:
        index = int(
            input("\nEnter Expense Number to Delete: ")
        ) - 1

        if 0 <= index < len(expenses):

            expenses.pop(index)

            save_expenses(expenses)

            print("Expense Deleted Successfully!")

        else:
            print("Invalid Expense Number")

    except ValueError:
        print("Invalid Input")


def main():

    expenses = load_expenses()

    while True:

        print("\n")
        print("=" * 40)
        print("        EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Report")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_report(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()