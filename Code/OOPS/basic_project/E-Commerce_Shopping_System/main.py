from amazon_store import AmazonStore
from customer import Customer
from seller import Seller
from product import Product


def main():

    # ==========================
    # Create Store
    # ==========================
    store = AmazonStore(
        "Amazon India",
        "Delhi",
        "Rahul Sharma"
    )

    print("\n===== STORE DETAILS =====")
    store.show_store()
    store.show_manager()

    # ==========================
    # Create Products
    # ==========================
    laptop = Product(
        101,
        "Laptop",
        "Electronics",
        "Dell",
        55000,
        10
    )

    mouse = Product(
        102,
        "Mouse",
        "Electronics",
        "Logitech",
        800,
        25
    )

    keyboard = Product(
        103,
        "Keyboard",
        "Electronics",
        "HP",
        1500,
        15
    )

    # ==========================
    # Create Seller
    # ==========================
    seller = Seller(
        1,
        "Amit",
        "amit@gmail.com",
        "9876543210",
        "Delhi"
    )

    print("\n===== SELLER DETAILS =====")
    seller.show_user()

    seller.add_product(laptop)
    seller.add_product(mouse)
    seller.add_product(keyboard)

    print("\nSeller Product List")
    seller.view_products()

    # ==========================
    # Add Products To Store
    # ==========================
    store.add_product(laptop)
    store.add_product(mouse)
    store.add_product(keyboard)

    # ==========================
    # Create Customer
    # ==========================
    customer = Customer(
        101,
        "Suraj",
        "suraj@gmail.com",
        "9999999999",
        "Bihar"
    )

    print("\n===== CUSTOMER DETAILS =====")
    customer.show_user()

    store.add_customer(customer)

    # ==========================
    # Customer Cart
    # ==========================
    customer.add_to_cart(laptop)
    customer.add_to_cart(mouse)

    print("\n===== CUSTOMER CART =====")
    customer.view_cart()

    # ==========================
    # Wishlist
    # ==========================
    customer.add_to_wishlist(keyboard)

    print("\n===== CUSTOMER WISHLIST =====")
    customer.view_wishlist()

    # ==========================
    # Place Order
    # ==========================
    customer.place_order(laptop)

    print("\n===== CUSTOMER ORDERS =====")
    customer.view_orders()

    store.add_order(laptop)

    # ==========================
    # Update Stock
    # ==========================
    laptop.reduce_stock(1)
    mouse.reduce_stock(2)

    # ==========================
    # Update Sales
    # ==========================
    seller.update_sales(laptop.price)
    seller.update_sales(mouse.price * 2)

    store.update_sales(laptop.price)
    store.update_sales(mouse.price * 2)

    print("\n===== SELLER SALES =====")
    seller.show_sales()

    print("\n===== STORE SALES =====")
    print(f"Total Store Sales : ₹{store.total_sales}")

    # ==========================
    # Product Details
    # ==========================
    print("\n===== PRODUCT DETAILS =====")
    laptop.show_product()
    mouse.show_product()
    keyboard.show_product()


if __name__ == "__main__":
    main()