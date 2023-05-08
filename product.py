import csv
from tabulate import tabulate


# Admin only can upload the products
class Products:
    all = []  # Object storing

    # Products details
    def __init__(self, name: str, barcode: int, brand: str, description: str, price: float, available=False):
        self.name = name
        self.barcode = barcode
        self.brand = brand
        self.description = description
        self.price = price
        self.available = available

        # Action to execute
        Products.all.append(self)

    # Save the products in the csv format
    @staticmethod
    def add_to_csv(name, barcode, brand, description, price, available):
        with open('products.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, barcode, brand, description, price, available])

    # display the products by table format
    @classmethod
    def display_products(cls):
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        print(tabulate(items, headers='keys', tablefmt='psql'))

    def __repr__(self):
        return f'Products("{self.name}", "{self.barcode}", "{self.brand}", "{self.description}", "{self.price}", "{self.available}")'


# product = Products("Product 1", 34567890, "Brand 1", "This is sample", 200, True)
# Products.add_to_csv(product.name, product.barcode, product.brand, product.description, product.price, product.available)

# Products.display_products()
