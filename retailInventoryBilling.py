# UC9 – Calculate Total Bill Amount Including All Items

inventory = {
    "apple": {"price": 30, "quantity": 100},
    "banana": {"price": 10, "quantity": 150},
    "milk": {"price": 50, "quantity": 40}
}

bill = []
total_bill = 0

print("Available Products:")
for product, details in inventory.items():
    print(product, "Price:", details["price"], "Quantity:", details["quantity"])

while True:

    product_name = input("\nEnter product name: ").lower()

    if product_name in inventory:

        quantity = int(input("Enter quantity: "))
        price = inventory[product_name]["price"]

        total_price = price * quantity
        total_bill += total_price

        bill.append({
            "product": product_name,
            "quantity": quantity,
            "total": total_price
        })

        print("Item added to bill.")

    else:
        print("Product not found.")

    choice = input("Add another item? (yes/no): ").lower()
    if choice != "yes":
        break

print("\n----- Bill Summary -----")
for item in bill:
    print(item["product"], "Qty:", item["quantity"], "Total:", item["total"])

print("\nTotal Bill Amount:", total_bill)