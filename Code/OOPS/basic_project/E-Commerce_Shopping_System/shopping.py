"""
                 <<Abstract Class>>
                    Shopping
              +----------------+
              | store_name     |
              | location       |
              +----------------+
              | show_store()   |
              | add_product()  |
              | remove_product()|
              +-------▲--------+
                      |
                      |
                AmazonStore
        +--------------------------+
        | manager_name             |
        | products[]               |
        | customers[]              |
        | orders[]                 |
        | total_sales              |
        +--------------------------+
        | add_product()            |
        | remove_product()         |
        | add_customer()           |
        | add_order()              |
        | update_sales()           |
        +--------------------------+


                         User
              +---------------------+
              | user_id             |
              | name                |
              | email               |
              | phone               |
              | address             |
              +---------------------+
              | show_user()         |
              +----------▲----------+
                         |
              -----------------------
              |                     |
              ▼                     ▼

        Customer                 Seller
 +----------------+        +----------------+
 | cart[]         |        | products[]     |
 | orders[]       |        | total_sales    |
 | wishlist[]     |        +----------------+
 +----------------+        | add_product()  |
 | add_to_cart()  |        | remove_product()|
 | place_order()  |        | view_products()|
 | view_orders()  |        | show_sales()   |
 +----------------+        +----------------+


                  Product
          +----------------+
          | product_id     |
          | name           |
          | category       |
          | brand          |
          | price          |
          | stock          |
          +----------------+
          | update_price() |
          | add_stock()    |
          | reduce_stock() |
          | show_product() |
          +----------------+
"""


from abc import ABC, abstractmethod
class Shopping(ABC):
    def __init__(self, store_name, location):
        self.store_name = store_name
        self.location = location
    
    def show_store(self):
        print("Store Name :", self.store_name)
        print("Store Location:", self.location)
    
    @abstractmethod
    def add_product(self):
        pass
    
    @abstractmethod
    def remove_product(self):
        pass