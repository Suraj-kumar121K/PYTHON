class Product:
    def __init__(self, product_id, name, category, brand, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        if new_price > 0:
            self.price = new_price
            print(f"{self.name} price updated successfully.")
        else:
            print("Invalid price.")

    def add_stock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            print(f"{quantity} units added.")
        else:
            print("Invalid quantity.")

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity} units sold.")
        else:
            print("Insufficient stock.")

    def is_available(self):
        return self.stock > 0

    def show_product(self):
        print("-" * 35)
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Category   : {self.category}")
        print(f"Brand      : {self.brand}")
        print(f"Price      : ₹{self.price}")
        print(f"Stock      : {self.stock}")
        print("-" * 35)

    def __str__(self):
        return f"{self.name} (₹{self.price})"