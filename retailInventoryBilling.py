# UC4 – Remove Product from Inventory

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 40}
}

product_name = input("Enter product name to remove: ").lower()

if product_name in inventory:
    del inventory[product_name]
    print("Product removed successfully.")
else:
    print("Product not found in inventory.")

print("\nUpdated Inventory:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])