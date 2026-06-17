# Farah Programming Exercise CSV-2 COP2373
# This program reads the grades.csv file and displays the data
# in a formatted table using the csv module.
# The program includes record counting, formatting, and repeatability.

import csv


# This function reads the CSV file and prints the data in a clean table.
# It also counts how many student records were found.
def display_grades():
    """
    Reads grades.csv and prints the data in a formatted table.
    """
    print("\n=== Student Grades ===\n")

    try:
        # Open the CSV file in read mode.
        with open("grades.csv", "r") as file:
            reader = csv.reader(file)

            # Read the header row so we can format the table correctly.
            header = next(reader)

            # Print the header with spacing for alignment.
            print(f"{header[0]:15}{header[1]:15}{header[2]:10}{header[3]:10}{header[4]:10}")
            print("-" * 60)

            # Loop through each student record and print it.
            count = 0
            for row in reader:
                count += 1
                print(f"{row[0]:15}{row[1]:15}{row[2]:10}{row[3]:10}{row[4]:10}")

            # Display how many records were found.
            print(f"\nTotal Records: {count}\n")

    except FileNotFoundError:
        # This message appears if Program 1 has not been run yet.
        print("ERROR: grades.csv not found. Please run Program 1 first.")

    # Pause so the instructor can read the output.
    input("Press Enter to continue...")


# This function allows the program to repeat.
# It lets the instructor view the table multiple times if needed.
def main():
    """
    Main loop to allow the program to repeat.
    """
    while True:
        display_grades()

        # Ask the instructor if they want to view the grades again.
        repeat = input("Would you like to view the grades again? (y/n): ").lower()
        if repeat != "y":
            print("\nExiting program. Goodbye!\n")
            break


# Run the program by calling main().
main()
