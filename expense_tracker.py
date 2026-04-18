import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
        
        from datetime import date as dt_date
        if not date:
            date = str(dt_date.today())
            
        expenses = load_expenses()
        expenses.append({"amount": amount, "category": category, "date": date})
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    total = 0
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp['date']} | {exp['category']}: ${exp['amount']:.2f}")
        total += exp['amount']
    print(f"-------------------")
    print(f"Total Spent: ${total:.2f}\n")

def main():
    while True:
        print("\n--- Simple Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
