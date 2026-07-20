from user import User
from user import User

class Seller(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone, address)

        self.products = []
        self.total_sales = 0

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            print(f"{product.name} added successfully.")
        else:
            print("Product already exists.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("Seller Products:")
            for product in self.products:
                print(product.name)

    def update_sales(self, amount):
        if amount > 0:
            self.total_sales += amount
            print("Sales updated.")
        else:
            print("Invalid amount.")

    def show_sales(self):
        print(f"Total Sales : ₹{self.total_sales}")