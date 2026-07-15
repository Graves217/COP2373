# Farah Programming Exercise CSV-1 COP2373
# This program allows an instructor to enter student names and exam grades.
# The program writes all student records to a CSV file named grades.csv.
# The program includes validation, formatting, and repeatability to ensure
# clean data entry and a smooth user experience.

import csv


# This function ensures the user enters a valid integer.
# It prevents crashes caused by typing letters or symbols.
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


# This function ensures exam grades fall within the valid range of 0–100.
# It prevents invalid grade values from being written to the CSV file.
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


# This function ensures names contain only alphabetic characters.
# It prevents numbers or symbols from being entered as names.
def get_name(prompt):
    """
    Gets a validated name containing only letters.
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name.capitalize()
        print("ERROR: Names must contain only letters.")


# This function collects all student information and writes it to grades.csv.
# It handles name validation, grade validation, and file writing.
def create_grades_file():
    """
    Collects student information and writes it to grades.csv.
    """
    print("\n=== Create Grades File ===\n")

    # Ask how many students the instructor wants to enter.
    student_count = get_integer("How many students would you like to enter? ")

    # Open the CSV file in write mode so old data is replaced with new data.
    # newline="" prevents blank lines from appearing in the CSV file.
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row so the CSV file is properly labeled.
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student and collect their information.
        for i in range(student_count):
            print(f"\nEntering data for student {i + 1}")

            # Get validated first and last names.
            first_name = get_name("Enter first name: ")
            last_name = get_name("Enter last name: ")

            # Get validated exam grades.
            exam1 = get_grade("Enter Exam 1 grade (0-100): ")
            exam2 = get_grade("Enter Exam 2 grade (0-100): ")
            exam3 = get_grade("Enter Exam 3 grade (0-100): ")

            # Write the student's record to the CSV file.
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv has been created successfully.\n")

    # Pause so the instructor can read the message before continuing.
    input("Press Enter to continue...")


# This function allows the entire program to repeat.
# It gives the instructor the option to enter more students without restarting the script.
def main():
    """
    Main loop to allow the program to repeat.
    """
    while True:
        create_grades_file()

        # Ask the instructor if they want to run the program again.
        repeat = input("Would you like to enter more students? (y/n): ").lower()
        if repeat != "y":
            print("\nExiting program. Goodbye!\n")
            break


# Run the program by calling main().
main()
