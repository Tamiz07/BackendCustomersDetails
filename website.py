from customer import CustomerDetails, Customer
from product import Products


class Website:
    def __init__(self):
        self.customer = Customer()
        self.product = Products
        
    # web page design
    def web_design(self):
        # This is the header portion of the design
        header = "Welcome to ShopKART!"
        print(header.center(80))
        param = "India's no.1 online shopping..!"
        print(param.center(80))
        reg = "New to our shopKART kindly Signup"
        print()
        print(reg)

    def signup(self):
        return self.customer.signup()

    def login(self):
        return self.customer.login()

    def show_product(self):
        return self.product.display_products()


web = Website()
web.web_design()
web.signup()
web.login()
web.show_product()
