def validate_price(price, product_name):
    """
    Validate the product price and convert it to a float.
    This prevents calculation errors when the price is not numeric.
    """
    try:
        # Convert the price to a float so numeric strings can still be used.
        converted_price = float(price)

        # Prevent negative prices because they are not valid for this program.
        if converted_price < 0:
            raise ValueError("Price cannot be negative.")

        return converted_price

    except ValueError:
        # Raise a clear error message to identify which product has bad data.
        raise ValueError(f"Invalid price for '{product_name}': {price}")


def validate_discount_rate(discount_rate, product_name):
    """
    Validate the discount rate and convert it to a float.
    This ensures the rate is between 0 and 1.
    """
    try:
        # Convert the discount rate to a float in case the value is entered differently.
        converted_discount_rate = float(discount_rate)

        # Prevent invalid discount rates outside the acceptable range.
        if converted_discount_rate < 0 or converted_discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")

        return converted_discount_rate

    except ValueError:
        # Raise a clear error message to identify which product has bad discount data.
        raise ValueError(
            f"Invalid discount rate for '{product_name}': {discount_rate}"
        )


def calculate_discount(price, discount_rate):
    """
    Calculate the discount amount based on the price and discount rate.
    """
    # Multiply the price by the discount rate to determine the discount amount.
    discount_amount = price * discount_rate

    return discount_amount


def apply_discount(price, discount_amount):
    """
    Apply the discount amount to the original price and return the final price.
    """
    # Subtract the discount amount from the original price.
    final_price = price - discount_amount

    return final_price


def display_product_summary(product_name, price, discount_amount, final_price):
    """
    Display the pricing summary for a product.
    """
    # Display the final results in a clean and readable format.
    print(f"Product: {product_name}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    print()


def process_product(product):
    """
    Process one product by validating values, calculating the discount,
    and displaying the final result.
    """
    # Store the product name so it can be used in messages and validation.
    product_name = product["name"]

    # Validate the price before calculations are performed.
    price = validate_price(product["price"], product_name)

    # Validate the discount rate before calculations are performed.
    discount_rate = validate_discount_rate(product["discount_rate"], product_name)

    # Calculate the discount using the validated values.
    discount_amount = calculate_discount(price, discount_rate)

    # Apply the discount to the original price.
    final_price = apply_discount(price, discount_amount)

    # Display the pricing summary for the current product.
    display_product_summary(product_name, price, discount_amount, final_price)


def main():
    """
    Run the discount processing program for each product.
    """
    # Store the product data in a list of dictionaries.
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # Process each product separately so one bad value does not stop the whole program.
    for product in products:
        try:
            # Process and display the current product information.
            process_product(product)

        except ValueError as error_message:
            # Display a meaningful error message if invalid data is found.
            print(f"Error processing product: {error_message}")
            print()


if __name__ == "__main__":
    main()