# Initialize an empty budget dictionary
budget = {}

# Function to add a category and budget amount
def add_category(category, amount):
    budget[category] = float(amount)

# Function to update a category's budget amount
def update_category(category, amount):
    if category in budget:
        budget[category] = float(amount)
    else:
        print("Category not found.")

# Function to view the budget
def view_budget():
    if budget:
        print("Budget Overview:")
        for category, amount in budget.items():
            print(f"{category}: ${amount:.2f}")
    else:
        print("No budget data available.")

# Function to track expenses
def track_expenses(category, expense):
    if category in budget:
        budget[category] -= float(expense)
    else:
        print("Category not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a budget category")
    print("2. Update a budget category")
    print("3. View budget")
    print("4. Track expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category name: ")
        amount = input("Enter budget amount: ")
        add_category(category, amount)
    elif choice == "2":
        category = input("Enter category name to update: ")
        amount = input("Enter new budget amount: ")
        update_category(category, amount)
    elif choice == "3":
        view_budget()
    elif choice == "4":
        category = input("Enter category name to track expenses: ")
        expense = input("Enter expense amount: ")
        track_expenses(category, expense)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
