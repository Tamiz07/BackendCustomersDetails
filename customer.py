import csv
from tabulate import tabulate


class CustomerDetails:
    # Customer details
    def __init__(self, firstname: str, lastname: str, email: str, phone: int, password: str):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.password = password

    @staticmethod
    def add_to_csv(firstname, lastname, email, phone, password):
        with open('customers.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([firstname, lastname, email, phone, password])

    @classmethod
    def display_items(cls):
        with open('customers.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        print(tabulate(items, headers='keys', tablefmt='psql'))

    # Object representation
    def __repr__(self):
        return f"CustomerDetails('{self.firstname}', '{self.lastname}', '{self.email}', '{self.phone}', '{self.password}')"


class Customer(CustomerDetails):
    def __init__(self):
        pass

    def signup(self):
        firstname = input("First name: ")
        lastname = input("Last name: ")

        while True:
            email = input("Email: ")
            # Check if email already exists in file
            with open('customers.csv', 'r') as file:
                reader = csv.reader(file)
                email_exists = False
                for row in reader:
                    if row[2] == email:
                        email_exists = True
                        break
                if email_exists:
                    print("This Email id already exists. Please choose another.")
                else:
                    break

        phone = int(input("Mobile no: "))
        password = input("Password: ")

        # Add new customer details to file
        self.add_to_csv(firstname, lastname, email, phone, password)
        print("Signup successfully.")

    def login(self):
        while True:
            email = input("Email: ")
            password = input("Password: ")
            with open('customers.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == email and row[4] == password:
                        print("Login successful!")
                        break
                else:
                    print("Invalid email or password")


# example usage
cus = Customer()
cus.signup()
cus.login()

print(CustomerDetails.display_items())
