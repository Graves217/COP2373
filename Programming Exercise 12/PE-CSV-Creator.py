# Farah Programming Exercise CSV-1 COP2373
# This program allows an instructor to enter student names and exam grades.
# The program writes all student records to a custom-named CSV file.
# The program includes validation, formatting, and repeatability.

import csv


def get_integer(prompt):
    """
    Gets a validated integer from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("ERROR: Please enter a valid integer.")


def get_grade(prompt):
    """
    Gets a validated exam grade between 0 and 100.
    """
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print("ERROR: Grade must be between 0 and 100.")
        except ValueError:
            print("ERROR: Please enter a valid integer.")


def get_name(prompt):
    """
    Gets a validated name containing only letters.
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name.capitalize()
        print("ERROR: Names must contain only letters.")


def get_filename():
    """
    Prompts the user for a CSV filename and ensures it is valid.
    Automatically appends .csv if the user does not include it.
    """
    while True:
        filename = input("Enter a name for the CSV file (without extension): ").strip()

        if filename == "":
            print("ERROR: Filename cannot be empty.")
            continue

        if not filename.lower().endswith(".csv"):
            filename += ".csv"

        return filename


def create_grades_file():
    """
    Collects student information and writes it to a custom CSV file.
    """
    print("\n=== Create Grades File ===\n")

    # Ask the instructor for a custom filename
    filename = get_filename()

    # Ask how many students to enter
    student_count = get_integer("How many students would you like to enter? ")

    # Open CSV file and write header
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop for each student
        for i in range(student_count):
            print(f"\nEntering data for student {i + 1}")

            first_name = get_name("Enter first name: ")
            last_name = get_name("Enter last name: ")

            exam1 = get_grade("Enter Exam 1 grade (0-100): ")
            exam2 = get_grade("Enter Exam 2 grade (0-100): ")
            exam3 = get_grade("Enter Exam 3 grade (0-100): ")

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\n{filename} has been created successfully.\n")
    input("Press Enter to continue...")


def main():
    """
    Main loop to allow the program to repeat.
    """
    while True:
        create_grades_file()

        repeat = input("Would you like to enter more students? (y/n): ").lower()
        if repeat != "y":
            print("\nExiting program. Goodbye!\n")
            break


# Run the program
main()
