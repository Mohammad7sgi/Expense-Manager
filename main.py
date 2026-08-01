import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


# Add a new expense
def add_expense():
    amount = int(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses = load_expenses()
    expenses.append(expense)

    save_expenses(expenses)

    print("✅ Expense added successfully!")


# Display all expenses
def show_expenses():
    expenses = load_expenses()

    if not expenses:
        print("❌ No expenses found.")
        return

    print("\nExpense List:")
    print("-" * 40)

    for item in expenses:
        print(
            f"Date: {item['date']} | "
            f"Category: {item['category']} | "
            f"Amount: {item['amount']} Toman"
        )


# Calculate today's total expenses
def daily_total():
    expenses = load_expenses()

    today = datetime.now().strftime("%Y-%m-%d")

    total = 0

    for item in expenses:
        if item["date"] == today:
            total += item["amount"]

    print(
        "Today's total expenses:",
        total,
        "Toman"
    )


# Calculate monthly total expenses
def monthly_total():
    expenses = load_expenses()

    month = datetime.now().strftime("%Y-%m")

    total = 0

    for item in expenses:
        if item["date"].startswith(month):
            total += item["amount"]

    print(
        "This month's total expenses:",
        total,
        "Toman"
    )


# Find the highest spending category
def highest_expense_category():
    expenses = load_expenses()

    categories = {}

    for item in expenses:
        category = item["category"]

        if category in categories:
            categories[category] += item["amount"]
        else:
            categories[category] = item["amount"]

    if not categories:
        print("❌ No expenses found.")
        return

    max_category = max(categories, key=categories.get)

    print("\nHighest spending category:")
    print(
        "Category:",
        max_category,
        "| Amount:",
        categories[max_category],
        "Toman"
    )


# Main menu
def menu():

    while True:

        print("""
=========================
 Expense Manager
=========================

1- Add Expense
2- Show Expenses
3- Today's Total
4- Monthly Total
5- Highest Spending Category
6- Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            daily_total()

        elif choice == "4":
            monthly_total()

        elif choice == "5":
            highest_expense_category()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("❌ Invalid option!")


menu()
