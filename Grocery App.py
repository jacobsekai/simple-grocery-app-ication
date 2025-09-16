inventory = []

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    expiration_date = int(input("Enter days until expiration: "))
    product = [name, quantity, price, expiration_date]
    inventory.append(product)
    print("Product added successfully.\n")

def update_quantity():
    name = input("Enter product name to update: ")
    for product in inventory:
        if product[0] == name:
            new_quantity = int(input("Enter new quantity: "))
            product[1] = new_quantity
            print("Quantity updated.\n")
            return
    print("Product not found.\n")

def about_to_expire():
    days = int(input("Enter number of days: "))
    print("Products expiring within", days, "days:")
    found = False
    for product in inventory:
        if product[3] <= days:
            print(product)
            found = True
    if not found:
        print("No products expiring soon.\n")

def total_value():
    total = 0
    for product in inventory:
        total += product[1] * product[2]
    print("Total stock value:", total, "\n")

def search_product():
    name = input("Enter product name to search: ")
    for product in inventory:
        if product[0] == name:
            print("Found:", product, "\n")
            return
    print("Product not found.\n")

while True:
    print("===== Grocery Store Inventory =====")
    print("1. Add new product")
    print("2. Update product quantity")
    print("3. Show products about to expire")
    print("4. Calculate total stock value")
    print("5. Search product by name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        about_to_expire()
    elif choice == "4":
        total_value()
    elif choice == "5":
        search_product()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
