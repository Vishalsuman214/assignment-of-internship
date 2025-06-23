bill = []

while True:
    print("\n1. Add item")
    print("2. Show bill")
    print("3. Show total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        bill.append([item, price, qty])

    elif choice == "2":
        print("\n--- Bill Items ---")
        total = 0
        for b in bill:
            item, price, qty = b
            amount = price * qty
            print(f"{item}: ${price} x {qty} = ${amount}")
            total += amount
        print(f"Total Amount: ₹{total}")

    elif choice == "3":
        total = sum(d[1] * d[2] for d in bill)
        print(f"Total Amount: &{total}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Enter 1 to 4.")
