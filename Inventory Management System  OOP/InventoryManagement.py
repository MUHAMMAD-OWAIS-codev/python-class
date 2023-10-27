class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def update_product_quantity(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = quantity
                return True
        return False

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for product in self.products:
                print(product)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Find Product")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)
            print("Product added to inventory.")

        elif choice == "2":
            product_id = int(input("Enter Product ID to remove: "))
            if inventory.remove_product(product_id):
                print("Product removed from inventory.")
            else:
                print("Product not found in inventory.")

        elif choice == "3":
            product_id = int(input("Enter Product ID to update quantity: "))
            new_quantity = int(input("Enter new quantity: "))
            if inventory.update_product_quantity(product_id, new_quantity):
                print("Quantity updated successfully.")
            else:
                print("Product not found in inventory.")

        elif choice == "4":
            product_id = int(input("Enter Product ID to find: "))
            product = inventory.find_product(product_id)
            if product:
                print(f"Found Product: {product}")
            else:
                print("Product not found in inventory.")

        elif choice == "5":
            inventory.display_inventory()

        elif choice == "6":
            print("Exiting the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
