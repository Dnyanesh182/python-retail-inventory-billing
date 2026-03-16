# UC6 – Select Product and Enter Purchase Quantity

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
        print("Product selected:", product_name)
        print("Quantity to purchase:", purchase_qty)
    else:
        print("Insufficient stock available.")
else:
    print("Product not found in inventory.")