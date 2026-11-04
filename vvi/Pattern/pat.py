from datetime import datetime
customers = {}
def add_customer(Name, Age, Phone, Location):

    # 2. Name Validation
    if not Name:
        print("Error: Customer Name is Required!")
        return

    # 3. Age Validation
    if not isinstance(Age, int) or Age <= 0 or Age > 120:
        print("Error: Invalid Customer Age!")
        return

    # 4. Phone Validation
    if not Phone.isdigit() or len(Phone) != 10:
        print("Error: Phone Number Must Be 10 Digits!")
        return

    # 5. Location Validation
    if not Location:
        print("Error: Location is Required!")
        return

    # 6. Duplicate Phone Check
    for customer in customers.values():
        if customer["Phone"] == Phone:
            print("Error: Phone Number Already Exists!")
            return

    # 7. Generate Customer ID
    customer_id = max(customers.keys(), default=100) + 1

    # 8. Customer Details
    Customers = {
        "Customer ID": customer_id,
        "Name": Name,
        "Age": Age,
        "Phone": Phone,
        "Location": Location,
        "Status": "New",
        "Registration Date": datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    # 9. Store Customer
    customers[customer_id] = Customers
    print("\nCustomer Added Successfully!")
    print("Customer ID:", customer_id)
    return Customers

def view_customers():
    if not customers:
        print("\nNo Customer Records Found!")
        return
    print("\n========== ALL CUSTOMERS ==========")
    for customer_id, details in customers.items():
        print("\nCustomer ID:", customer_id)
        print("Name:", details["Name"])
        print("Age:", details["Age"])
        print("Phone:", details["Phone"])
        print("Location:", details["Location"])
        print("Status:", details["Status"])
        print("Registration Date:", details["Registration Date"])
        print("-" * 40)
    
def main():
    menu = {
        1: "Add Customer",
        2: "View Customers",
        3: "Search Customer",
        4: "Update Customer",
        5: "Delete Customer",
        6: "Update Customer Status",
        7: "Exit"
    }

    while True:

        print("\n========== CRM SYSTEM ==========")

        for key, value in menu.items():
            print(f"{key}. {value}")

        try:
            choice = int(input("\nEnter Your Choice: "))

            if choice == 1:
                Name = input("Enter a Name: ")
                Age = int(input("Enter an Age: "))
                Phone = input("Enter a Phone No: ")
                Location = input("Enter a Location: ")
                add_customer(Name, Age, Phone, Location)
                
                Add_Customer = input("\nAdd Another Customer? (yes/no): ")
                if Add_Customer.lower() != "yes":
                    break
                print("\n========== ALL CUSTOMERS ==========")
                for customer_id, details in customers.items():
                    print(details)
                
            elif choice == 2:
                view_customers()

            elif choice == 3:
                search_customer()

            elif choice == 4:
                update_customer()

            elif choice == 5:
                delete_customer()

            elif choice == 6:
                update_status()

            elif choice == 7:
                print("Thank You For Using CRM System!")
                break
            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter a Valid Number!")

if __name__ == "__main__":
    main()