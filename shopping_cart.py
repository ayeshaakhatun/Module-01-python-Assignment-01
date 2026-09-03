# 1. Take customer name input
customer_name = input("Enter customer name: ")

# 2. Take names and prices of 3 products
product1 = input("Product 1: ")
price1 = int(input("Price: "))

product2 = input("Product 2: ")
price2 = int(input("Price: "))

product3 = input("Product 3: ")
price3 = int(input("Price: "))

# 3. Calculate subtotal
subtotal = price1 + price2 + price3

# 4. Determine discount percentage and calculate discount & final total
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discount = subtotal * discount_rate
final_total = subtotal - discount

# Round decimal values before printing
discount = round(discount, 2)
final_total = round(final_total, 2)

# 5. Display shopping summary
print(f"\nCustomer Name: {customer_name}")
print(f"Product 1: {product1}")
print(f"Price: {price1}")
print(f"Product 2: {product2}")
print(f"Price: {price2}")
print(f"Product 3: {product3}")
print(f"Price: {price3}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")