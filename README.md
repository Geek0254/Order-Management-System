                    Overview Description
                    
This python code uses the mysql.connector module to interact with a MySQL database. 
It has two main functions: Adding an order to the database, and Updating the delivery status of an order in the database. 
It uses the tkinter library to create a graphical user interface (GUI) that allows the user to interact with the database.

                    Steps to run the code   

Install the required packages: mysql.connector and tkinter using: pip install mysql-connector-python and pip install python-tk, respectively.
Start a local MySQL server, such as XAMPP.
Connect to the database by providing the host, user, password, and database name in the mysql.connector.connect method. 
If you are using XAMPP, the host is usually "localhost", the user is "root", and the password is left empty.

Create the database and table for the orders by executing the following SQL commands in the XAMPP control panel:

CREATE DATABASE dopestcollections;
USE dopestcollections;
CREATE TABLE orders (OrderID INT AUTO_INCREMENT PRIMARY KEY, ProductName VARCHAR(25), Quantity INT, Amount FLOAT, PhoneNumber VARCHAR(15), DeliveryAddress VARCHAR(30), DeliveryDate DATETIME, DeliveryStatus VARCHAR(10));

Run the Python script using python filename.py in the terminal or command prompt. 
This will launch the GUI, which consists of two buttons: "Add Order" and "Update Status". Clicking on either button will open a new window where you can enter the details for the order.

To add an order, enter the product name, quantity, amount, phone number, and delivery address in the "Add Order" window, then click the "Add" button. The order will be added to the database. The order ID is set to auto increment (starting from 1,2,3...) which can be used for referencing when updating the status.
To update the delivery status, enter the order ID, delivery status, and delivery date in the "Update Status" window, then click the "Update" button. The delivery status will be updated in the database.
