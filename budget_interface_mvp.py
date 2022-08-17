from budget import Budget
import pprint


def pickBudget(budgets):
    print("Which budget do you want to add categories to?")
    pprint.pprint(active_budgets)

    return input()


"""
Constants
"""
active_budgets = {}

while True:
    print("Enter command:\n" +
          "Create new budget: 1\n" +
          "Set categories for a budget: 2\n" +
          "Add categories to a budget: 3\n" +
          "Print a budget: 4\n" +
          "Delete a buget: 5\n" +
          "Exit app: q"
          )

    user_input = input()

    if user_input == 'q':
        break

    if user_input == '4':
        if not active_budgets:
            print("\nYou need to create a budget first.")
            continue

        budget = pickBudget

        print(active_budgets[budget])

    if user_input == '3':
        if not active_budgets:
            print("\nYou need to create a budget first.")
            continue

        user_input = pickBudget(active_budgets)

        active_budgets[user_input].addCategories()

    elif user_input == '2':
        if not active_budgets:
            print("\nYou need to create a budget first.")
            continue

        user_input = pickBudget(active_budgets)

        active_budgets[user_input].setCategories()

    elif user_input == '1':
        print("What should this budget be called?")
        budget_name = input()

        new_budget = Budget(budget_name)

        active_budgets[str(len(active_budgets) + 1)] = new_budget

        pprint.pprint(active_budgets)


def pickBudget(budgets):
    print("Which budget do you want to add categories to?")
    pprint.pprint(active_budgets)

    return input()
