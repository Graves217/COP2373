# Anthony Farah
# Cinema Ticket Pre-Sale Program
# This program pre-sells a limited number of cinema tickets. Each buyer may
# purchase up to 4 tickets, and no more than 20 tickets can be sold total.
# The program tracks remaining tickets and counts the total number of buyers.
# The program is repeatable so the user may run it again.


# Function to handle a single ticket purchase
def process_purchase(remaining_tickets):
    """
    Handles one buyer's ticket request and returns the updated number of tickets.
    """

    # Ask the user how many tickets they want to buy
    requested = int(input("How many tickets would you like to buy (1-4)? "))

    # Validate the request to ensure it follows the rules
    if requested < 1 or requested > 4:
        print("You may only purchase between 1 and 4 tickets.\n")
        return remaining_tickets

    # Check if enough tickets remain for this purchase
    if requested > remaining_tickets:
        print("Not enough tickets remain for that purchase.\n")
        return remaining_tickets

    # Subtract the purchased tickets from the remaining total
    remaining_tickets -= requested

    # Display updated ticket count
    print(f"Tickets remaining: {remaining_tickets}\n")

    return remaining_tickets


# Main function to run the ticket-selling loop
def main():
    """
    Controls the overall ticket-selling process until all tickets are sold.
    Allows the user to repeat the entire program.
    """

    # Loop to allow the entire program to repeat
    repeat_program = "y"

    while repeat_program.lower() == "y":

        # Total number of tickets available at the start
        remaining_tickets = 10

        # Accumulator to count how many buyers purchased tickets
        buyer_count = 0

        # Loop until all tickets are sold
        while remaining_tickets > 0:

            # Process one buyer's purchase and update remaining tickets
            remaining_tickets = process_purchase(remaining_tickets)

            # Increase buyer count only when a purchase attempt occurs
            buyer_count += 1

        # Display the total number of buyers once all tickets are sold
        print("All tickets have been sold.")
        print(f"Total number of buyers: {buyer_count}\n")

        # Ask the user if they want to run the program again
        repeat_program = input("Would you like to run the program again? (y/n): ")
        print()  # Blank line for readability


# Call the main function to start the program
if __name__ == "__main__":
    main()
