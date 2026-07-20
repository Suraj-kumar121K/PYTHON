from user import User
class Customer(User):
    def __init__(self, user_id, name, email, phone, address):
        super().__init__(user_id, name, email, phone, address)
        self.cart = []
        self.orders = []
        self.wishlist = []
        
    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            for product in self.cart:
                print(product.name)

    def place_order(self, order):
        self.orders.append(order)

    def view_orders(self):
        if not self.orders:
            print("No orders found.")
        else:
            for order in self.orders:
                print(order)

    def add_to_wishlist(self, product):
        self.wishlist.append(product)

    def view_wishlist(self):
        if not self.wishlist:
            print("Wishlist is empty.")
        else:
            for product in self.wishlist:
                print(product.name)
            
    