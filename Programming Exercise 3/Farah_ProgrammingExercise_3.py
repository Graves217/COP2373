# Name: Anthony Farah
# Date: June 6, 2026
# Assignment: Programming Exercise - Monthly Expenses

# This program allows the user to enter monthly expenses.
# It calculates the total, highest, and lowest expenses using reduce().
# The program repeats so the user can perform multiple calculations
# without restarting the program.


from functools import reduce


def get_expenses():
    """
    Collects expense types and amounts from the user.
    """

    expenses_list = []

    # Loop allows the user to enter multiple expenses.
    # It continues until the user types "done".
    while True:
        expense_type = input(
            "Enter expense type (or 'done' to finish): "
        )

        if expense_type.lower() == "done":
            break

        try:
            amount = float(
                input(f"Enter amount for {expense_type}: ")
            )

            # This condition ensures the expense is valid.
            # Expenses must be positive because they represent costs.
            # Zero or negative values do not make sense in this context.
            if amount <= 0:
                print("Expense must be greater than 0.")
                print("Please enter a positive number.")
                continue

            # Store data as a tuple (expense type and amount)
            expenses_list.append((expense_type, amount))

        except ValueError:
            # Prevents crashes if the user enters invalid input.
            print("Invalid input. Please enter a number.")

    return expenses_list


def calculate_total(expenses):
    """
    Calculates the total of all expenses using reduce().
    """

    # reduce() adds each expense amount to a running total.
    return reduce(lambda total, x: total + x[1], expenses, 0)


def find_highest(expenses):
    """
    Finds the highest expense.
    """

    # reduce() compares values and keeps the highest one.
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


def find_lowest(expenses):
    """
    Finds the lowest expense.
    """

    # reduce() compares values and keeps the lowest one.
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)


def main():
    """
    Controls program execution and allows repetition.
    """

    # Outer loop lets the user repeat the entire program.
    while True:
        expenses = get_expenses()

        if not expenses:
            print("No expenses entered.")
        else:
            total = calculate_total(expenses)
            highest = find_highest(expenses)
            lowest = find_lowest(expenses)

            print("\n--- Expense Summary ---")
            print(f"Total Expenses: ${total:.2f}")

            print(
                f"Highest Expense: {highest[0]} - ${highest[1]:.2f}"
            )

            print(
                f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}"
            )

        repeat = input(
            "\nWould you like to enter another set of expenses? "
            "(yes/no): "
        )

        # If the user does not type "yes", exit the program.
        if repeat.lower() != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()