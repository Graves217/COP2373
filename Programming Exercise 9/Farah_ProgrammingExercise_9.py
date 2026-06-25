# -------------------------------------------------------------
# COP2373 – Programming Exercise 9
# Author: Anthony Farah
# Description:
#   This program defines a BankAcct class that models a simple
#   bank account. The class supports depositing, withdrawing,
#   adjusting interest rates, calculating interest, and showing
#   account information. The program includes:
#
#   - Input validation helper functions
#   - A transaction log to record activity
#   - A menu-driven loop for repeatability
#   - Type hints for clarity
#   - Currency formatting helper
#
#   All code is placed inside functions to meet course rules.
#   Comments follow PEP 8 guidelines and explain WHY actions
#   are taken, not just what they do.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Helper function to format currency consistently.
# This improves readability and ensures all money displays
# in a professional format.
# -------------------------------------------------------------
def format_money(amount: float) -> str:
    return f"${amount:,.2f}"


# -------------------------------------------------------------
# Helper function to validate positive numeric input.
# This prevents invalid values from entering the system.
# -------------------------------------------------------------
def validate_positive(value: float) -> bool:
    return value > 0


# -------------------------------------------------------------
# BankAcct Class Definition
# -------------------------------------------------------------
class BankAcct:
    # ---------------------------------------------------------
    # __init__ sets up the initial state of the account.
    # We also create a transaction log to track activity.
    # ---------------------------------------------------------
    def __init__(self, name: str, acct_num: str, amount: float, interest_rate: float):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate
        self.transactions = []  # Stores a history of actions

    # ---------------------------------------------------------
    # deposit adds money to the account after validating that
    # the amount is positive. We also log the transaction.
    # ---------------------------------------------------------
    def deposit(self, amt: float) -> None:
        if validate_positive(amt):
            self.amount += amt
            self.transactions.append(f"Deposited {format_money(amt)}")
        else:
            print("Deposit amount must be positive.")

    # ---------------------------------------------------------
    # withdraw removes money from the account if:
    #   - The amount is positive
    #   - There are sufficient funds
    # We log successful withdrawals.
    # ---------------------------------------------------------
    def withdraw(self, amt: float) -> None:
        if not validate_positive(amt):
            print("Withdrawal amount must be positive.")
        elif amt > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amt
            self.transactions.append(f"Withdrew {format_money(amt)}")

    # ---------------------------------------------------------
    # adjust_interest_rate updates the interest rate after
    # validating that the new rate is not negative.
    # ---------------------------------------------------------
    def adjust_interest_rate(self, new_rate: float) -> None:
        if new_rate >= 0:
            self.interest_rate = new_rate
            self.transactions.append(f"Interest rate changed to {new_rate * 100:.2f}%")
        else:
            print("Interest rate cannot be negative.")

    # ---------------------------------------------------------
    # calculate_interest computes interest earned over a number
    # of days using the simple interest formula.
    # We do not modify the balance here.
    # ---------------------------------------------------------
    def calculate_interest(self, days: int) -> float:
        if days < 0:
            print("Days cannot be negative.")
            return 0
        interest = self.amount * self.interest_rate * (days / 365)
        self.transactions.append(f"Calculated {format_money(interest)} interest for {days} days")
        return interest

    # ---------------------------------------------------------
    # get_balance returns the current account balance.
    # ---------------------------------------------------------
    def get_balance(self) -> float:
        return self.amount

    # ---------------------------------------------------------
    # show_transactions prints the transaction history.
    # This helps users understand what actions occurred.
    # ---------------------------------------------------------
    def show_transactions(self) -> None:
        print("\nTransaction Log:")
        for t in self.transactions:
            print(" -", t)
        print()

    # ---------------------------------------------------------
    # __str__ returns a formatted string representation of the
    # account. This is used whenever the object is printed.
    # ---------------------------------------------------------
    def __str__(self) -> str:
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: {format_money(self.amount)}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")


# -------------------------------------------------------------
# Function to display the menu options.
# This keeps the main loop clean and readable.
# -------------------------------------------------------------
def display_menu() -> None:
    print("\n=== BANK ACCOUNT MENU ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Adjust Interest Rate")
    print("5. Calculate Interest")
    print("6. Show Transaction Log")
    print("7. Exit")


# -------------------------------------------------------------
# Menu-driven test function.
# This makes the program repeatable and interactive.
# -------------------------------------------------------------
def test_bank_acct() -> None:
    # Create a sample account for testing
    acct = BankAcct("Anthony", "123456", 1000.00, 0.05)

    print("=== PROGRAMMING EXERCISE 9 OUTPUT ===")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            acct.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter withdrawal amount: "))
            acct.withdraw(amt)

        elif choice == "3":
            print("Current Balance:", format_money(acct.get_balance()))

        elif choice == "4":
            new_rate = float(input("Enter new interest rate (decimal): "))
            acct.adjust_interest_rate(new_rate)

        elif choice == "5":
            days = int(input("Enter number of days: "))
            interest = acct.calculate_interest(days)
            print("Interest Earned:", format_money(interest))

        elif choice == "6":
            acct.show_transactions()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------
if __name__ == "__main__":
    test_bank_acct()