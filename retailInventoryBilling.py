# UC10 – Print Final Bill with Product Details and Total Amount

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
            "price": price,
            "total": total_price
        })

        print("Item added to bill.")

    else:
        print("Product not found.")

    choice = input("Add another item? (yes/no): ").lower()
    if choice != "yes":
        break


print("\n========== FINAL BILL ==========")
print("Product\tQty\tPrice\tTotal")

for item in bill:
    print(f"{item['product']}\t{item['quantity']}\t{item['price']}\t{item['total']}")

print("--------------------------------")
print("Total Bill Amount:", total_bill)
print("================================")