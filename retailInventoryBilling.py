# UC5 – Display Available Products in Inventory

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 40}
}

print("Available Products in Inventory:\n")

for product, details in inventory.items():
    print(f"Product: {product}")
    print(f"Price: {details['price']}")
    print(f"Quantity: {details['quantity']}")
    print("-----------------------")