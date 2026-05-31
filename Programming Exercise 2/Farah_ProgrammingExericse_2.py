# Farah_ProgrammingExericse_2.py

def calculate_spam_score(message, keywords):
    """
    Calculate spam score based on occurrences of keywords.
    Returns (score, matched_keywords_list).
    """
    message_lower = message.lower()
    score = 0
    matched = []

    for word in keywords:
        count = message_lower.count(word.lower())
        if count > 0:
            score += count
            matched.append((word, count))

    return score, matched


def rate_spam(score):
    """
    Return a text rating based on the spam score.
    """
    if score <= 2:
        return "Unlikely to be spam"
    elif score <= 6:
        return "Possibly spam"
    elif score <= 12:
        return "Likely spam"
    else:
        return "Almost certainly spam"


def get_message_from_user():
    """
    Collects a multi-line email message from the user.
    """
    print("Enter your email message. Press Enter on an empty line to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    spam_keywords = [
        "free", "winner", "congratulations", "act now", "limited time",
        "urgent", "risk-free", "guaranteed", "no obligation", "click here",
        "call now", "order now", "money-back", "earn extra cash",
        "work from home", "be your own boss", "make money fast", "get rich",
        "credit card", "low interest", "debt relief", "cheap", "discount",
        "special offer", "prize", "100% free", "no credit check",
        "act immediately", "limited offer", "exclusive deal"
    ]

    while True:
        message = get_message_from_user()

        score, matched = calculate_spam_score(message, spam_keywords)
        rating = rate_spam(score)

        print("\n--- Spam Analysis Result ---")
        print(f"Spam score: {score}")
        print(f"Likelihood: {rating}")

        if matched:
            print("\nWords/phrases that contributed to the spam score:")
            for word, count in matched:
                print(f"- '{word}' (found {count} time(s))")
        else:
            print("\nNo spam keywords found in the message.")

        again = input("\nWould you like to analyze another message? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
