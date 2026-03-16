# UC1 – Initialize Product Inventory

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 50}
}

print("Product Inventory:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])