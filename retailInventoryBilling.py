# UC3 – Update Product Quantity in Inventory

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 40}
}

product_name = input("Enter product name to update quantity: ").lower()

if product_name in inventory:
    new_quantity = int(input("Enter new quantity: "))
    inventory[product_name]["quantity"] = new_quantity
    print("Product quantity updated successfully.")
else:
    print("Product not found in inventory.")

print("\nUpdated Inventory:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])