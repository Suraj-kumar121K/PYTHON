"""
Shopping Cart
Concepts:
list
append()
remove()
loop

Features:
Add Product
Remove Product
View Cart
"""

"""
cart = []

def add_product():
    product = input("Enter Product Name: ")
    cart.append(product)
    print("Product Added")

def view_project():
    if len(cart) == 0:
        print("Cart Empty")
    else:
        print("\nCart Items")
        for item in cart:
            print(item)
            
def remove_product():
    product = input("Enter Product Name Remove: ")
    if product in cart:
        cart.remove(product)
        print("Product Removed")
    else:
        print("Product Not Found")
    
while True:
    print("\n ----- Shoping Cart ----")
    print("1. Add Project")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Exit")
    choice = input("Enter Choice:")
    if choice == "1":
        add_product()
    elif choice == "2":
        view_project()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        print("Program Closed")
        break
    else:
        print("Invalid Choice")
""" 
        