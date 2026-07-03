import random

# ------------------------------------------------------------
# Deck class from Section 11.5 of the textbook.
# This class simulates a deck of numbered cards (0–51).
# The deck automatically reshuffles when empty.
# ------------------------------------------------------------
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")
        self.current_card += 1
        return self.card_list[self.current_card - 1]


# ------------------------------------------------------------
# Rank and suit lists used to convert card numbers.
# ------------------------------------------------------------
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'J', 'Q', 'K', 'A']

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']


# ------------------------------------------------------------
# Convert a card number (0–51) into a readable card.
# FIXED: suit_index must use % 4, not % 13.
# ------------------------------------------------------------
def convert_card(card_number):
    rank_index = card_number // 13
    suit_index = card_number % 4
    return RANKS[rank_index], SUITS[suit_index]


# ------------------------------------------------------------
# Deal a poker hand of five cards.
# ------------------------------------------------------------
def deal_hand(deck):
    return [deck.deal() for _ in range(5)]


# ------------------------------------------------------------
# Replace selected cards in the hand.
# ------------------------------------------------------------
def replace_cards(hand, deck, indices):
    for index in indices:
        pos = index - 1
        if 0 <= pos < len(hand):
            hand[pos] = deck.deal()
    return hand


# ------------------------------------------------------------
# Print a poker hand with readable card names.
# ------------------------------------------------------------
def print_hand(hand, title):
    print(f"\n--- {title} ---")
    for i, card in enumerate(hand, start=1):
        rank, suit = convert_card(card)
        print(f"{i}: {rank} of {suit}")


# ------------------------------------------------------------
# Validate user input for card replacement.
# ------------------------------------------------------------
def get_valid_indices():
    user_input = input(
        "\nEnter card numbers to replace (e.g., 1 3 5), "
        "or press Enter to keep all cards: "
    ).strip()

    if not user_input:
        return []

    try:
        indices = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. No cards will be replaced.")
        return []

    valid_indices = [i for i in indices if 1 <= i <= 5]

    if len(valid_indices) != len(indices):
        print("Some numbers were invalid and ignored.")

    return valid_indices


# ------------------------------------------------------------
# Determine the ranking of a poker hand.
# ------------------------------------------------------------
def rank_hand(hand):
    ranks = []
    suits = []

    for card in hand:
        rank, suit = convert_card(card)
        ranks.append(rank)
        suits.append(suit)

    rank_values = [RANKS.index(r) for r in ranks]
    rank_values.sort()

    rank_counts = {r: ranks.count(r) for r in ranks}
    suit_counts = {s: suits.count(s) for s in suits}

    is_flush = max(suit_counts.values()) == 5
    is_straight = rank_values == list(range(rank_values[0], rank_values[0] + 5))

    if is_flush and rank_values == [8, 9, 10, 11, 12]:
        return "Royal Flush"

    if is_flush and is_straight:
        return "Straight Flush"

    if 4 in rank_counts.values():
        return "Four of a Kind"

    if sorted(rank_counts.values()) == [2, 3]:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if 3 in rank_counts.values():
        return "Three of a Kind"

    if list(rank_counts.values()).count(2) == 2:
        return "Two Pair"

    if 2 in rank_counts.values():
        return "One Pair"

    return "High Card"


# ------------------------------------------------------------
# Display menu options to the user.
# ------------------------------------------------------------
def show_menu():
    print("\n--- Poker Menu ---")
    print("1. Deal a new hand")
    print("2. View ranking rules")
    print("3. Exit")


# ------------------------------------------------------------
# Print ranking rules for the user.
# ------------------------------------------------------------
def show_ranking_rules():
    print("\n--- Poker Hand Rankings ---")
    print("Royal Flush")
    print("Straight Flush")
    print("Four of a Kind")
    print("Full House")
    print("Flush")
    print("Straight")
    print("Three of a Kind")
    print("Two Pair")
    print("One Pair")
    print("High Card")


# ------------------------------------------------------------
# Main game loop with menu system.
# ------------------------------------------------------------
def main():
    print("Welcome to the Poker Hand Simulator!")

    while True:
        show_menu()
        choice = input("\nPlease select an option (1–3): ").strip()

        if choice == "1":
            deck = Deck(52)
            hand = deal_hand(deck)
            print_hand(hand, "Initial Poker Hand")

            indices = get_valid_indices()
            hand = replace_cards(hand, deck, indices)

            print_hand(hand, "Final Poker Hand")

            ranking = rank_hand(hand)
            print(f"\nYour hand ranking is: {ranking}")

        elif choice == "2":
            show_ranking_rules()

        elif choice == "3":
            print("\nThank you for playing!")
            break

        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


# ------------------------------------------------------------
# Run the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
