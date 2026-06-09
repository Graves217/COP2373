# Anthony Programming Exercise 7
# This enhanced program allows the user to enter a paragraph and then
# extracts, cleans, and displays each sentence using non-greedy regular
# expressions. It also validates input and formats the output cleanly.
# The program now includes repeatability so the user can run it multiple times.

import re


# -------------------------------------------------------------
# Function: get_paragraph
# Prompts the user to enter a paragraph of text.
# Ensures the user does not enter a blank paragraph.
# -------------------------------------------------------------
def get_paragraph():
    paragraph = input("Please enter a paragraph: ").strip()

    # Ensuring the user enters something meaningful
    while paragraph == "":
        print("You must enter a paragraph. Please try again.")
        paragraph = input("Please enter a paragraph: ").strip()

    return paragraph


# -------------------------------------------------------------
# Function: extract_sentences
# Uses a non-greedy regular expression to find each sentence.
# A sentence ends with '.', '?', or '!'.
# Returns a list of raw sentences.
# -------------------------------------------------------------
def extract_sentences(paragraph):
    pattern = r'.*?[.!?]'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL)
    return sentences


# -------------------------------------------------------------
# Function: clean_sentence
# Removes extra whitespace and newline characters from a sentence.
# -------------------------------------------------------------
def clean_sentence(sentence):
    cleaned = sentence.strip()
    cleaned = " ".join(cleaned.split())  # Normalizes internal spacing
    return cleaned


# -------------------------------------------------------------
# Function: clean_all_sentences
# Applies clean_sentence to each sentence in the list.
# Filters out any empty results.
# -------------------------------------------------------------
def clean_all_sentences(sentences):
    cleaned_list = []

    for s in sentences:
        cleaned = clean_sentence(s)
        if cleaned != "":
            cleaned_list.append(cleaned)

    return cleaned_list


# -------------------------------------------------------------
# Function: count_sentences
# Returns the number of sentences in the list.
# -------------------------------------------------------------
def count_sentences(sentences):
    return len(sentences)


# -------------------------------------------------------------
# Function: display_results
# Displays each cleaned sentence and the total count.
# -------------------------------------------------------------
def display_results(sentences):
    print("\n----- Extracted Sentences -----\n")

    for sentence in sentences:
        print(sentence)

    print("\nTotal number of sentences:", count_sentences(sentences))


# -------------------------------------------------------------
# Function: ask_to_repeat
# Asks the user if they want to run the program again.
# Returns True to repeat, False to exit.
# -------------------------------------------------------------
def ask_to_repeat():
    choice = input("\nWould you like to analyze another paragraph? (y/n): ").strip().lower()

    while choice not in ("y", "n"):
        print("Invalid input. Please enter 'y' or 'n'.")
        choice = input("Would you like to analyze another paragraph? (y/n): ").strip().lower()

    return choice == "y"


# -------------------------------------------------------------
# Function: main
# Controls the flow of the program and allows repeatability.
# -------------------------------------------------------------
def main():
    keep_running = True

    while keep_running:
        paragraph = get_paragraph()
        raw_sentences = extract_sentences(paragraph)
        cleaned_sentences = clean_all_sentences(raw_sentences)
        display_results(cleaned_sentences)

        keep_running = ask_to_repeat()

    print("\nThank you for using the Sentence Extractor Program!")


# Start the program
main()
