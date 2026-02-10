# Simple Expense Tracker
#  python project 1
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print("Expense added.\n")

def show_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- Expense List ---")
    for i, (name, amount) in enumerate(expenses, start=1):
        print(f"{i}. {name} - Rs {amount}")
    print()

def show_total():
    total = sum(amount for _, amount in expenses)
    print(f"Total spent: Rs {total}\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Choose an option: ")
    # condition applies here , suiii
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")
