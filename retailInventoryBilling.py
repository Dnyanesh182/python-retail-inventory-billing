# UC7 – Calculate Item Price Based on Quantity

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 40}
}

print("Available Products:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])

product_name = input("\nEnter product name to purchase: ").lower()

if product_name in inventory:
    purchase_qty = int(input("Enter quantity to purchase: "))

    if purchase_qty <= inventory[product_name]["quantity"]:
        price = inventory[product_name]["price"]
        total_price = price * purchase_qty

        print("Product:", product_name)
        print("Unit Price:", price)
        print("Quantity:", purchase_qty)
        print("Total Price:", total_price)
    else:
        print("Insufficient stock available.")
else:
    print("Product not found.")