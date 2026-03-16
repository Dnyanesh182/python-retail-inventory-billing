# UC2 – Add New Product to Inventory

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150}
}

product_name = input("Enter product name: ").lower()
price = int(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

if product_name in inventory:
    print("Product already exists in inventory.")
else:
    inventory[product_name] = {"price": price, "quantity": quantity}
    print("Product added successfully.")

print("\nUpdated Inventory:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])