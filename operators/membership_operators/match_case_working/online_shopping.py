"""
3. Online Shopping – Coupon Check
------------------------------------
Task:
- Ask for coupon code

If coupon code is valid:
    - Ask for cart amount
    - If amount ≥ 1000:
        "Coupon applied"
    - Else:
        "Minimum purchase not met"
Else:
    "Invalid coupon"
"""
coupon_code = "save10"
user_coupon = input("Enter coupon code: ")
if user_coupon == coupon_code:
    cart_amount =int(input("Enter total cart amount: "))
    if cart_amount >= 1000:
        print("Coupon applied")
    else:
        print("Minimum purchase not met")
else:
    print("Invalid coupon")