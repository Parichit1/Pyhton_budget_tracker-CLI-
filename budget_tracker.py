import json


def add_expenses(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expenses: {description} for amount {amount}")


def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum


def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print(f"Expenses : {expenses}")
    for expense in expenses:
        print(f"{expense['description']} : {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")


def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses}
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    print("Welcome to my Budget tracking app.")
    filepath = 'budget_tracker.json'
    initial_budget, expenses = load_budget_data(filepath)

    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget

    while True:
        print("What would you like to do? \n")
        print("1. Add an expense \n")
        print("2. Show budget details \n")
        print("3. Exit  \n")
        choice = int(input("Please select your choice (1/2/3): "))

        if choice == 1:
            description = input("Please enter expense description: ")
            amount = float(input("Please enter the expense amount: "))
            add_expenses(expenses, description, amount)
        elif choice == 2:
            show_budget_details(budget, expenses)
        elif choice == 3:
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting the budget app. Thanks for using.")
            break

        else:
            print("Invalid choice please select (1/2/3)")


if __name__ == "__main__":
    main()
