import re

# ---------------------------------------------------------
# validate_phone:
# This function validates US phone numbers. It removes all
# non-digit characters, checks if the number is valid for
# the United States, and formats it as (123) 456-7890.
# It accepts:
#   - 10-digit US numbers
#   - 11-digit numbers starting with country code '1'
# It returns a formatted phone number or a detailed error.
# ---------------------------------------------------------
def validate_phone(phone):
    # Remove all non-digit characters from the input
    digits = re.sub(r'\D', '', phone)

    # Ensure the cleaned string contains only digits
    if not digits.isdigit():
        return None, "Phone number contains invalid characters."

    # Handle 11-digit numbers that start with the US country code '1'
    if len(digits) == 11:
        if digits[0] == '1':
            digits = digits[1:]  # Strip the country code
        else:
            return None, "Only US phone numbers are accepted (country code must be 1)."

    # Validate that the remaining number has exactly 10 digits
    if len(digits) < 10:
        return None, "Phone number has too few digits (needs 10)."

    if len(digits) > 10:
        return None, "Phone number has too many digits (US numbers must be 10 digits)."

    # Format the valid 10-digit number into (123) 456-7890
    area = digits[0:3]
    mid = digits[3:6]
    last = digits[6:10]
    formatted_phone = f"({area}) {mid}-{last}"

    return formatted_phone, None


# ---------------------------------------------------------
# validate_ssn:
# This function validates Social Security Numbers by
# removing all non-digit characters and ensuring exactly
# 9 digits remain. If valid, it formats the SSN as
# 123-45-6789. Otherwise, it returns a detailed error.
# ---------------------------------------------------------
def validate_ssn(ssn):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', ssn)

    # Ensure only digits remain
    if not digits.isdigit():
        return None, "SSN contains invalid characters."

    # SSNs must contain exactly 9 digits
    if len(digits) < 9:
        return None, "SSN has too few digits (needs 9)."

    if len(digits) > 9:
        return None, "SSN has too many digits (needs 9)."

    # Format the SSN into 123-45-6789
    part1 = digits[0:3]
    part2 = digits[3:5]
    part3 = digits[5:9]
    formatted_ssn = f"{part1}-{part2}-{part3}"

    return formatted_ssn, None


# ---------------------------------------------------------
# validate_zip:
# This function validates ZIP codes by removing all
# non-digit characters and ensuring the result contains
# either 5 digits (standard ZIP) or 9 digits (ZIP+4).
# It returns the formatted ZIP or a detailed error.
# ---------------------------------------------------------
def validate_zip(zip_code):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', zip_code)

    # Ensure only digits remain
    if not digits.isdigit():
        return None, "ZIP code contains invalid characters."

    # ZIP codes must contain either 5 or 9 digits
    if len(digits) not in (5, 9):
        return None, "ZIP code must have 5 or 9 digits."

    # Format 5-digit ZIP
    if len(digits) == 5:
        return digits, None

    # Format ZIP+4 as 12345-6789
    formatted_zip = f"{digits[0:5]}-{digits[5:9]}"
    return formatted_zip, None


# ---------------------------------------------------------
# main:
# This function controls the program flow. It repeatedly
# prompts the user for a phone number, SSN, and ZIP code,
# validates and formats each one, and displays either the
# formatted result or a detailed error message.
# The loop continues until the user chooses to exit.
# ---------------------------------------------------------
def main():
    print("=== Input Validation and Formatting Program ===")

    while True:
        # Prompt the user for all three inputs
        phone = input("\nEnter a phone number: ")
        ssn = input("Enter a social security number: ")
        zip_code = input("Enter a ZIP code: ")

        # Validate and format each input
        formatted_phone, phone_error = validate_phone(phone)
        formatted_ssn, ssn_error = validate_ssn(ssn)
        formatted_zip, zip_error = validate_zip(zip_code)

        # Display results
        print("\n--- Results ---")

        print("Phone Number:")
        print(f"  {formatted_phone if formatted_phone else phone_error}")

        print("SSN:")
        print(f"  {formatted_ssn if formatted_ssn else ssn_error}")

        print("ZIP Code:")
        print(f"  {formatted_zip if formatted_zip else zip_error}")

        # Ask user if they want to run the program again
        again = input("\nWould you like to validate another set? (y/n): ").strip().lower()
        if again != 'y':
            print("\nExiting program. Goodbye.")
            break


# ---------------------------------------------------------
# Program entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
