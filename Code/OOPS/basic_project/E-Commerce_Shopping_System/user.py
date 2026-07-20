class User:
    def __init__(self, user_id, name, email, phone, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def show_user(self):
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Phone   : {self.phone}")
        print(f"Address : {self.address}")