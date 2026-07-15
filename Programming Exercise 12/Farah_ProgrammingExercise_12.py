# -------------------------------------------------------------
# Import required modules for numerical analysis and CSV reading
# -------------------------------------------------------------
import numpy as np
import csv


# -------------------------------------------------------------
# Function: choose_file
# Purpose: Allow the user to browse and select a CSV file.
# Why: Makes the program more user-friendly and flexible.
# -------------------------------------------------------------
def choose_file() -> str:
    """
    Open a file dialog so the user can select a CSV file.

    Returns:
        str: The full path to the selected CSV file.
    """
    import tkinter as tk
    from tkinter import filedialog

    # Create a hidden root window for the file dialog
    root = tk.Tk()
    root.withdraw()

    # Open the file dialog
    file_path = filedialog.askopenfilename(
        title="Select your grades CSV file",
        filetypes=[("CSV Files", "*.csv")]
    )

    return file_path


# -------------------------------------------------------------
# Function: load_grades
# Purpose: Load exam grades from a CSV file into a NumPy array.
# Why: NumPy arrays allow fast statistical calculations.
# -------------------------------------------------------------
def load_grades(file_name: str) -> np.ndarray:
    """
    Load exam grades from a CSV file and return a NumPy array.

    Parameters:
        file_name (str): The name of the CSV file.

    Returns:
        numpy.ndarray: Array containing exam grades.
    """
    data = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            # Convert exam grade columns into integers
            exams = list(map(int, row[2:]))
            data.append(exams)

    return np.array(data)


# -------------------------------------------------------------
# Function: print_dataset_preview
# Purpose: Display the first few rows of the dataset.
# Why: Helps the user understand the structure of the data.
# -------------------------------------------------------------
def print_dataset_preview(grades: np.ndarray) -> None:
    """
    Print the first five rows of the dataset.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    print("\nDataset Preview:")
    for row in grades[:5]:
        print(row)


# -------------------------------------------------------------
# Function: exam_statistics
# Purpose: Calculate and display statistics for each exam.
# Why: Helps understand performance on individual exams.
# -------------------------------------------------------------
def exam_statistics(grades: np.ndarray) -> None:
    """
    Calculate and print statistics for each exam.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    num_exams = grades.shape[1]

    print("\n=== Exam Statistics ===")
    for i in range(num_exams):
        exam = grades[:, i]
        print(f"\nExam {i + 1}:")
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Standard Deviation: {np.std(exam):.2f}")
        print(f"Minimum: {np.min(exam)}")
        print(f"Maximum: {np.max(exam)}")


# -------------------------------------------------------------
# Function: overall_statistics
# Purpose: Calculate statistics across all exams combined.
# Why: Shows overall class performance.
# -------------------------------------------------------------
def overall_statistics(grades: np.ndarray) -> None:
    """
    Calculate and print overall statistics across all exams.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    all_grades = grades.flatten()

    print("\n=== Overall Statistics (All Exams Combined) ===")
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")


# -------------------------------------------------------------
# Function: pass_fail_statistics
# Purpose: Count passes and fails for each exam and compute
#          overall pass percentage.
# Why: Helps measure student success rates.
# -------------------------------------------------------------
def pass_fail_statistics(grades: np.ndarray) -> None:
    """
    Calculate and print pass/fail counts for each exam and overall
    pass percentage.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    num_exams = grades.shape[1]
    passing_grade = 60
    total_passes = 0
    total_grades = grades.size

    print("\n=== Pass/Fail Statistics ===")

    for i in range(num_exams):
        exam = grades[:, i]
        passes = np.sum(exam >= passing_grade)
        fails = np.sum(exam < passing_grade)
        total_passes += passes

        print(f"\nExam {i + 1}:")
        print(f"Passed: {passes}")
        print(f"Failed: {fails}")

    overall_pass_percentage = (total_passes / total_grades) * 100
    print(f"\nOverall Pass Percentage Across All Exams: "
          f"{overall_pass_percentage:.2f}%")


# -------------------------------------------------------------
# Function: summary_report
# Purpose: Print a combined summary of all statistics.
# Why: Provides a clean final overview for the user.
# -------------------------------------------------------------
def summary_report(grades: np.ndarray) -> None:
    """
    Print a full summary report including exam statistics,
    overall statistics, and pass/fail results.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    print("\n==============================")
    print("        SUMMARY REPORT        ")
    print("==============================")

    exam_statistics(grades)
    overall_statistics(grades)
    pass_fail_statistics(grades)

    print("\nEnd of Summary Report.")


# -------------------------------------------------------------
# Function: menu
# Purpose: Provide a menu system for user interaction.
# Why: Allows user to choose which analysis to run.
# -------------------------------------------------------------
def menu(grades: np.ndarray) -> None:
    """
    Display a menu and allow the user to choose an analysis option.

    Parameters:
        grades (numpy.ndarray): The array of exam grades.
    """
    while True:
        print("\n=== Grade Analysis Menu ===")
        print("1. View Exam Statistics")
        print("2. View Overall Statistics")
        print("3. View Pass/Fail Statistics")
        print("4. View Full Summary Report")
        print("5. View Dataset Preview")
        print("6. Exit Menu")

        choice = input("Please enter your choice (1-6): ")

        if choice == "1":
            exam_statistics(grades)
        elif choice == "2":
            overall_statistics(grades)
        elif choice == "3":
            pass_fail_statistics(grades)
        elif choice == "4":
            summary_report(grades)
        elif choice == "5":
            print_dataset_preview(grades)
        elif choice == "6":
            print("\nExiting menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# -------------------------------------------------------------
# Function: main
# Purpose: Coordinate program execution.
# Why: Keeps code organized and readable.
# -------------------------------------------------------------
def main() -> None:
    """
    Main function to load data, validate structure, and run menu.
    """
    print("\nPlease select your grades CSV file.")
    file_name = choose_file()

    if not file_name:
        print("\nNo file selected. Please try again.")
        return

    try:
        grades = load_grades(file_name)
    except FileNotFoundError:
        print(f"\nError: The file '{file_name}' was not found.")
        return

    if grades.shape[1] < 1:
        print("\nError: No exam columns found in the CSV file.")
        return

    menu(grades)


# -------------------------------------------------------------
# Repeatability Loop
# Purpose: Allow user to run the program multiple times.
# -------------------------------------------------------------
while True:
    main()

    while True:
        repeat = input("\nWould you like to run the analysis again? (yes/no): ")
        repeat = repeat.lower()

        if repeat in ("yes", "no"):
            break

        print("Invalid input. Please type 'yes' or 'no'.")

    if repeat == "no":
        print("\nProgram ended. Thank you for using the grade analyzer.")
        break
