import re

# ---------------------------------------------------------
# validate_phone:
# Validates US phone numbers. Removes all non-digit
# characters, checks for correct digit count, and formats
# the number as (123) 456-7890. Accepts 10-digit US numbers
# or 11-digit numbers beginning with country code '1'.
# Returns formatted number or a detailed error message.
# ---------------------------------------------------------
def validate_phone(phone):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)

    # Ensure only digits remain
    if not digits.isdigit():
        return None, "Phone number contains invalid characters."

    # Handle 11-digit numbers starting with US country code '1'
    if len(digits) == 11:
        if digits[0] == '1':
            digits = digits[1:]  # Strip the country code
        else:
            return None, "Only US phone numbers are accepted (country code must be 1)."

    # Validate 10-digit US number
    if len(digits) < 10:
        return None, "Phone number has too few digits (needs 10)."

    if len(digits) > 10:
        return None, "Phone number has too many digits (US numbers must be 10 digits)."

    # Format into (123) 456-7890
    area = digits[0:3]
    mid = digits[3:6]
    last = digits[6:10]
    formatted_phone = f"({area}) {mid}-{last}"

    return formatted_phone, None


# ---------------------------------------------------------
# validate_ssn:
# Validates Social Security Numbers. Removes all non-digit
# characters, ensures exactly 9 digits remain, and formats
# the SSN as 123-45-6789. Returns formatted SSN or error.
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

    # Format into 123-45-6789
    part1 = digits[0:3]
    part2 = digits[3:5]
    part3 = digits[5:9]
    formatted_ssn = f"{part1}-{part2}-{part3}"

    return formatted_ssn, None


# ---------------------------------------------------------
# validate_zip:
# Validates ZIP codes. Removes all non-digit characters and
# ensures the result contains either 5 digits (standard ZIP)
# or 9 digits (ZIP+4). Formats ZIP+4 as 12345-6789.
# ---------------------------------------------------------
def validate_zip(zip_code):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', zip_code)

    # Ensure only digits remain
    if not digits.isdigit():
        return None, "ZIP code contains invalid characters."

    # ZIP codes must contain 5 or 9 digits
    if len(digits) not in (5, 9):
        return None, "ZIP code must have 5 or 9 digits."

    # Format 5-digit ZIP
    if len(digits) == 5:
        return digits, None

    # Format ZIP+4
    formatted_zip = f"{digits[0:5]}-{digits[5:9]}"
    return formatted_zip, None


# ---------------------------------------------------------
# main:
# Controls program flow. Prompts user for phone, SSN, and
# ZIP code, validates and formats each one, and displays
# results using a clear Valid/Invalid label. Repeats until
# the user chooses to exit.
# ---------------------------------------------------------
def main():
    print("=== Input Validation and Formatting Program ===")

    while True:
        # Prompt user for input
        phone = input("\nEnter a phone number: ")
        ssn = input("Enter a social security number: ")
        zip_code = input("Enter a ZIP code: ")

        # Validate and format each input
        formatted_phone, phone_error = validate_phone(phone)
        formatted_ssn, ssn_error = validate_ssn(ssn)
        formatted_zip, zip_error = validate_zip(zip_code)

        # Display results in the requested format
        print("\n--- Results ---")

        if formatted_phone:
            print(f"Phone Number (Valid): {formatted_phone}")
        else:
            print(f"Phone Number (Invalid): {phone_error}")

        if formatted_ssn:
            print(f"SSN (Valid): {formatted_ssn}")
        else:
            print(f"SSN (Invalid): {ssn_error}")

        if formatted_zip:
            print(f"ZIP Code (Valid): {formatted_zip}")
        else:
            print(f"ZIP Code (Invalid): {zip_error}")

        # Ask user if they want to run again
        again = input("\nWould you like to validate another set? (y/n): ").strip().lower()
        if again != 'y':
            print("\nExiting program. Goodbye.")
            break


# ---------------------------------------------------------
# Program entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
