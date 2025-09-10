import ecommerce_utils as eu

cart = {}
n = int(input("Enter the number of items to add: "))
for i in range(n):
    productname = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    cart[productname] = price

eu.apply_discount(1000, 10)
eu.add_gst(1000, 18)

