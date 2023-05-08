from customer import CustomerDetails, Customer
from product import Products


class Website:
    def __init__(self):
        self.customer = Customer()
        self.product = Products

    def signup(self):
        return self.customer.signup()

    def login(self):
        return self.customer.login()

    def show_product(self):
        return self.product.display_products()


web = Website()
web.signup()
web.login()
web.show_product()
