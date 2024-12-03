import csv
import random
from datetime import datetime, timedelta

# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Order class
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    def print_order(self):
        print(f"Order ID: {self.order_id}")
        for product in self.products:
            print(f"\tProduct: {product.name}, Price: {product.price:.2f}")
        print(f"Total Price: {self.total_price():.2f}\n")

# Customer class
class Customer:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)

# Store class
class Store:
    def __init__(self, store_id):
        self.store_id = store_id
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer

    def record_order(self, customer, order):
        self.add_customer(customer)
        self.customers[customer.customer_id].create_order(order)

# Corporation class
class Corporation:
    def __init__(self, name):
        self.name = name
        self.stores = {}

    def add_store(self, store):
        if store.store_id not in self.stores:
            self.stores[store.store_id] = store

    def record_sale(self, store_id, customer, order):
        if store_id in self.stores:
            self.stores[store_id].record_order(customer, order)
        else:
            print(f"Error: Store {store_id} not found in Corporation")

    def generate_sales_report(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write CSV headers
                writer.writerow([
                    "Date", "Time", "StoreID", "CustomerID", "OrderID", 
                    "Products (Name:Price)", "Total Price"
                ])
                
                for store_id, store in self.stores.items():
                    for customer_id, customer in store.customers.items():
                        for order in customer.orders:
                            order_date = datetime.now() - timedelta(days=random.randint(0, 365))
                            # Combine all products in the order into a single string
                            products_info = ", ".join([f"{product.name}:{product.price}" for product in order.products])
                            # Write a single row for the entire order
                            writer.writerow([
                                order_date.strftime("%Y-%m-%d"),  # Date
                                order_date.strftime("%H:%M:%S"),  # Time
                                store_id,                         # StoreID
                                customer_id,                      # CustomerID
                                order.order_id,                   # OrderID
                                products_info,                    # Products (Name:Price)
                                f"{order.total_price():.2f}"              # Total Price of the Order
                            ])
            print(f"Sales report successfully generated in {filename}")
        except Exception as e:
            print(f"Error generating sales report: {e}")

# List of 50 U.S. states as Store names
us_states = [
    "Ignacio's Alabama 1", "Ignacio's Alabama 2", "Ignacio's Alabama 3", "Ignacio's Alabama 4", "Ignacio's Alabama 5",
    "Ignacio's Alaska 1", "Ignacio's Alaska 2", "Ignacio's Alaska 3", "Ignacio's Alaska 4", "Ignacio's Alaska 5",
    "Ignacio's Arizona 1", "Ignacio's Arizona 2", "Ignacio's Arizona 3", "Ignacio's Arizona 4", "Ignacio's Arizona 5",
    "Ignacio's Arkansas 1", "Ignacio's Arkansas 2", "Ignacio's Arkansas 3", "Ignacio's Arkansas 4", "Ignacio's Arkansas 5",
    "Ignacio's California 1", "Ignacio's California 2", "Ignacio's California 3", "Ignacio's California 4", "Ignacio's California 5",
    "Ignacio's Colorado 1", "Ignacio's Colorado 2", "Ignacio's Colorado 3", "Ignacio's Colorado 4", "Ignacio's Colorado 5",
    "Ignacio's Connecticut 1", "Ignacio's Connecticut 2", "Ignacio's Connecticut 3", "Ignacio's Connecticut 4", "Ignacio's Connecticut 5",
    "Ignacio's Delaware 1", "Ignacio's Delaware 2", "Ignacio's Delaware 3", "Ignacio's Delaware 4", "Ignacio's Delaware 5",
    "Ignacio's Florida 1", "Ignacio's Florida 2", "Ignacio's Florida 3", "Ignacio's Florida 4", "Ignacio's Florida 5",
    "Ignacio's Georgia 1", "Ignacio's Georgia 2", "Ignacio's Georgia 3", "Ignacio's Georgia 4", "Ignacio's Georgia 5",
    "Ignacio's Hawaii 1", "Ignacio's Hawaii 2", "Ignacio's Hawaii 3", "Ignacio's Hawaii 4", "Ignacio's Hawaii 5",
    "Ignacio's Idaho 1", "Ignacio's Idaho 2", "Ignacio's Idaho 3", "Ignacio's Idaho 4", "Ignacio's Idaho 5",
    "Ignacio's Illinois 1", "Ignacio's Illinois 2", "Ignacio's Illinois 3", "Ignacio's Illinois 4", "Ignacio's Illinois 5",
    "Ignacio's Indiana 1", "Ignacio's Indiana 2", "Ignacio's Indiana 3", "Ignacio's Indiana 4", "Ignacio's Indiana 5",
    "Ignacio's Iowa 1", "Ignacio's Iowa 2", "Ignacio's Iowa 3", "Ignacio's Iowa 4", "Ignacio's Iowa 5",
    "Ignacio's Kansas 1", "Ignacio's Kansas 2", "Ignacio's Kansas 3", "Ignacio's Kansas 4", "Ignacio's Kansas 5",
    "Ignacio's Kentucky 1", "Ignacio's Kentucky 2", "Ignacio's Kentucky 3", "Ignacio's Kentucky 4", "Ignacio's Kentucky 5",
    "Ignacio's Louisiana 1", "Ignacio's Louisiana 2", "Ignacio's Louisiana 3", "Ignacio's Louisiana 4", "Ignacio's Louisiana 5",
    "Ignacio's Maine 1", "Ignacio's Maine 2", "Ignacio's Maine 3", "Ignacio's Maine 4", "Ignacio's Maine 5",
    "Ignacio's Maryland 1", "Ignacio's Maryland 2", "Ignacio's Maryland 3", "Ignacio's Maryland 4", "Ignacio's Maryland 5",
    "Ignacio's Massachusetts 1", "Ignacio's Massachusetts 2", "Ignacio's Massachusetts 3", "Ignacio's Massachusetts 4", "Ignacio's Massachusetts 5",
    "Ignacio's Michigan 1", "Ignacio's Michigan 2", "Ignacio's Michigan 3", "Ignacio's Michigan 4", "Ignacio's Michigan 5",
    "Ignacio's Minnesota 1", "Ignacio's Minnesota 2", "Ignacio's Minnesota 3", "Ignacio's Minnesota 4", "Ignacio's Minnesota 5",
    "Ignacio's Mississippi 1", "Ignacio's Mississippi 2", "Ignacio's Mississippi 3", "Ignacio's Mississippi 4", "Ignacio's Mississippi 5",
    "Ignacio's Missouri 1", "Ignacio's Missouri 2", "Ignacio's Missouri 3", "Ignacio's Missouri 4", "Ignacio's Missouri 5",
    "Ignacio's Montana 1", "Ignacio's Montana 2", "Ignacio's Montana 3", "Ignacio's Montana 4", "Ignacio's Montana 5",
    "Ignacio's Nebraska 1", "Ignacio's Nebraska 2", "Ignacio's Nebraska 3", "Ignacio's Nebraska 4", "Ignacio's Nebraska 5",
    "Ignacio's Nevada 1", "Ignacio's Nevada 2", "Ignacio's Nevada 3", "Ignacio's Nevada 4", "Ignacio's Nevada 5",
    "Ignacio's New Hampshire 1", "Ignacio's New Hampshire 2", "Ignacio's New Hampshire 3", "Ignacio's New Hampshire 4", "Ignacio's New Hampshire 5",
    "Ignacio's New Jersey 1", "Ignacio's New Jersey 2", "Ignacio's New Jersey 3", "Ignacio's New Jersey 4", "Ignacio's New Jersey 5",
    "Ignacio's New Mexico 1", "Ignacio's New Mexico 2", "Ignacio's New Mexico 3", "Ignacio's New Mexico 4", "Ignacio's New Mexico 5",
    "Ignacio's New York 1", "Ignacio's New York 2", "Ignacio's New York 3", "Ignacio's New York 4", "Ignacio's New York 5",
    "Ignacio's North Carolina 1", "Ignacio's North Carolina 2", "Ignacio's North Carolina 3", "Ignacio's North Carolina 4", "Ignacio's North Carolina 5",
    "Ignacio's North Dakota 1", "Ignacio's North Dakota 2", "Ignacio's North Dakota 3", "Ignacio's North Dakota 4", "Ignacio's North Dakota 5",
    "Ignacio's Ohio 1", "Ignacio's Ohio 2", "Ignacio's Ohio 3", "Ignacio's Ohio 4", "Ignacio's Ohio 5",
    "Ignacio's Oklahoma 1", "Ignacio's Oklahoma 2", "Ignacio's Oklahoma 3", "Ignacio's Oklahoma 4", "Ignacio's Oklahoma 5",
    "Ignacio's Oregon 1", "Ignacio's Oregon 2", "Ignacio's Oregon 3", "Ignacio's Oregon 4", "Ignacio's Oregon 5",
    "Ignacio's Pennsylvania 1", "Ignacio's Pennsylvania 2", "Ignacio's Pennsylvania 3", "Ignacio's Pennsylvania 4", "Ignacio's Pennsylvania 5",
    "Ignacio's Rhode Island 1", "Ignacio's Rhode Island 2", "Ignacio's Rhode Island 3", "Ignacio's Rhode Island 4", "Ignacio's Rhode Island 5",
    "Ignacio's South Carolina 1", "Ignacio's South Carolina 2", "Ignacio's South Carolina 3", "Ignacio's South Carolina 4", "Ignacio's South Carolina 5",
    "Ignacio's South Dakota 1", "Ignacio's South Dakota 2", "Ignacio's South Dakota 3", "Ignacio's South Dakota 4", "Ignacio's South Dakota 5",
    "Ignacio's Tennessee 1", "Ignacio's Tennessee 2", "Ignacio's Tennessee 3", "Ignacio's Tennessee 4", "Ignacio's Tennessee 5",
    "Ignacio's Texas 1", "Ignacio's Texas 2", "Ignacio's Texas 3", "Ignacio's Texas 4", "Ignacio's Texas 5",
    "Ignacio's Utah 1", "Ignacio's Utah 2", "Ignacio's Utah 3", "Ignacio's Utah 4", "Ignacio's Utah 5",
    "Ignacio's Vermont 1", "Ignacio's Vermont 2", "Ignacio's Vermont 3", "Ignacio's Vermont 4", "Ignacio's Vermont 5",
    "Ignacio's Virginia 1", "Ignacio's Virginia 2", "Ignacio's Virginia 3", "Ignacio's Virginia 4", "Ignacio's Virginia 5",
    "Ignacio's Washington 1", "Ignacio's Washington 2", "Ignacio's Washington 3", "Ignacio's Washington 4", "Ignacio's Washington 5",
    "Ignacio's West Virginia 1", "Ignacio's West Virginia 2", "Ignacio's West Virginia 3", "Ignacio's West Virginia 4", "Ignacio's West Virginia 5",
]

# Create some sample data
corporation = Corporation("Ignacio's Mexican Food")

# Sample products
product_list = [
    Product("Nachos", 9.99),
    Product("Quesadilla", 7.99),
    Product("Burrito", 8.99),
    Product("Taco", 4.99),
    Product("Salsa", 0.99),
    Product("Breakfast Taco", 3.99),
    Product("Agua Fresca", 2.99),
    Product("Breakfast Burrito", 8.99),
    Product("Soda Pop", 1.99),
]

# Sample stores named after U.S. states
for state in us_states:
    store = Store(state)  # Use the state name as the store ID
    corporation.add_store(store)

# Sample customers and orders
for customer_id in range(1, 2001):  # Create 2000 customers
    customer = Customer(f"Customer_{customer_id}")
    print(f"\nCustomer {customer.customer_id} is making orders:")
    for _ in range(random.randint(1, 5)):  # Each customer makes 1-5 orders
        order = Order(f"Order_{random.randint(1000, 9999)}")
        for _ in range(random.randint(1, 9)):  # Each order has 1-9 products
            product = random.choice(product_list)
            order.add_product(product)
        order.print_order()  # Print out the order details
        # Randomly assign store for each order
        store_id = random.choice(us_states)
        if store_id not in corporation.stores:
            print(f"Warning: Store {store_id} not found.")
        corporation.record_sale(store_id, customer, order)

# Generate sales report for the year
corporation.generate_sales_report("ignacio's_corporation_sales_data.csv")
