from shopping import Shopping
class AmazonStore(Shopping):
    def __init__(self, store_name, location, manager_name):
        super().__init__(store_name, location)
        self.manager_name = manager_name
        self.products = []
        self.orders = []
        self.customers = []
        self.total_sales = 0
        
    def show_manager(self):
        print(f"Manager Name : {self.manager_name}")
    
    def add_product(self, product):
        # Duplicate product add hone se rokta hai.
        if product not in self.products:
            self.products.append(product)
            print(f"{product} added successfully.")
        else:
            print(f"{product} already exists.")
    
    def remove_product(self, products):
        # Sirf wahi product remove karta hai jo list me maujood ho.
        if products in self.products:
            self.products.remove(products)
            print(f"{products} removed successfully.")
        else:
            print(f"{products} not found.")
    
    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)
            print(f"{order} placed successfully.")
        else:
            print(f"{order} already exists.")
        
    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
        else:
            print("Customer already exists.")
        
    def update_sales(self, amount):
        if amount > 0:
            self.total_sales += amount
        else:
            print("Invalid amount.")
        