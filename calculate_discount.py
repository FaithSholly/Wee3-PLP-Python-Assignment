# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied if less than 20%
        return price


# --- Main program starts here ---
# Ask user for original price and discount
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")