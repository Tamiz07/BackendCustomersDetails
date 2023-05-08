# Customer Details And Products

The CustomerDetails class stores the details of each customer including their first and last name, email, phone number, and password. The Customer class is a subclass of CustomerDetails and it provides methods for customer signup and login. When a customer signs up, their details are saved in the CSV file named customers.csv. The login method allows the customer to enter their email and password and checks if they exist in the customers.csv file. If the login is successful, the method prints "Login successful!".

The Products class stores details of each product, including name, barcode, brand, description, price, and availability. It provides methods for adding new products and displaying all products available for sale. When a new product is added, it is stored in the CSV file named products.csv.

The Website class is the main class that contains instances of the Customer and Products classes. It provides methods for customer signup, login, and displaying the available products.
