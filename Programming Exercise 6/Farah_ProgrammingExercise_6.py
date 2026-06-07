import re

# ---------------------------------------------------------
# validate_phone: checks if a phone number matches formats
# such as 123-456-7890, (123) 456-7890, 1234567890, etc.
# ---------------------------------------------------------
def validate_phone(phone):
    pattern = r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$'
    return bool(re.match(pattern, phone))


# ---------------------------------------------------------
# validate_ssn: checks if SSN matches the format 123-45-6789
# ---------------------------------------------------------
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


# ---------------------------------------------------------
# validate_zip: checks if ZIP is 5 digits or ZIP+4 format
# ---------------------------------------------------------
def validate_zip(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


# ---------------------------------------------------------
# main: repeatable loop that gets user input and displays
# validation results until the user chooses to exit
# ---------------------------------------------------------
def main():
    print("=== Input Validation Program ===")

    while True:
        phone = input("\nEnter a phone number: ")
        ssn = input("Enter a social security number: ")
        zip_code = input("Enter a ZIP code: ")

        print("\n--- Validation Results ---")
        print(f"Phone Number Valid: {validate_phone(phone)}")
        print(f"SSN Valid: {validate_ssn(ssn)}")
        print(f"ZIP Code Valid: {validate_zip(zip_code)}")

        # Ask user if they want to run again
        again = input("\nWould you like to validate another set? (y/n): ").strip().lower()
        if again != 'y':
            print("\nExiting program. Goodbye.")
            break


# ---------------------------------------------------------
# Call main
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
