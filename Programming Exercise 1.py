# Anthony Farah
# Cinema Ticket Pre-Sale Program
# This program pre-sells a limited number of cinema tickets. Each buyer may
# purchase up to 4 tickets, and no more than 20 tickets can be sold total.
# The program tracks remaining tickets and counts the total number of buyers.


# Function to handle a single ticket purchase
def process_purchase(remaining_tickets):
    """
    Handles one buyer's ticket request and returns the updated number of tickets.
    """

    # Ask the user how many tickets they want to buy
    # We ask inside this function so each buyer interaction is self-contained
    requested = int(input("How many tickets would you like to buy (1–4)? "))

    # Validate the request to ensure it follows the rules
    if requested < 1 or requested > 4:
        print("You may only purchase between 1 and 4 tickets.")
        return remaining_tickets

    # Check if enough tickets remain for this purchase
    if requested > remaining_tickets:
        print("Not enough tickets remain for that purchase.")
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
    """

    # Total number of tickets available at the start
    remaining_tickets = 20

    # Accumulator to count how many buyers purchased tickets
    buyer_count = 0

    # Loop until all tickets are sold
    while remaining_tickets > 0:

        # Process one buyer's purchase and update remaining tickets
        remaining_tickets = process_purchase(remaining_tickets)

        # Increase buyer count only when a valid purchase attempt occurs
        buyer_count += 1

    # Display the total number of buyers once all tickets are sold
    print(f"All tickets have been sold.")
    print(f"Total number of buyers: {buyer_count}")


# Call the main function to start the program
if __name__ == "__main__":
    main()
