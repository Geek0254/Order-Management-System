import mysql.connector
import tkinter as tk

# Connect to the database
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dopestcollections"
)

# Create the main window
root = tk.Tk()
root.title("Order Management System")

# Create the "Add Order" window
def add_order_window():
  add_window = tk.Toplevel(root)
  add_window.title("Add Order")
  
  # Create the fields for product name, quantity, amount, phone number, and delivery address
  product_label = tk.Label(add_window, text="Product Name")
  product_entry = tk.Entry(add_window)
  quantity_label = tk.Label(add_window, text="Quantity")
  quantity_entry = tk.Entry(add_window)
  amount_label = tk.Label(add_window, text="Amount")
  amount_entry = tk.Entry(add_window)
  phone_label = tk.Label(add_window, text="Phone Number")
  phone_entry = tk.Entry(add_window)
  address_label = tk.Label(add_window, text="Delivery Address")
  address_entry = tk.Entry(add_window)
  
  # Create the button to add the order to the database
  add_button = tk.Button(add_window, text="Add", command=lambda: add_order(product_entry.get(), quantity_entry.get(), amount_entry.get(), phone_entry.get(), address_entry.get()))
  
  # Place the fields and button in the window
  product_label.grid(row=0, column=0)
  product_entry.grid(row=0, column=1)
  quantity_label.grid(row=1, column=0)
  quantity_entry.grid(row=1, column=1)
  amount_label.grid(row=2, column=0)
  amount_entry.grid(row=2, column=1)
  phone_label.grid(row=3, column=0)
  phone_entry.grid(row=3, column=1)
  address_label.grid(row=4, column=0)
  address_entry.grid(row=4, column=1)
  add_button.grid(row=5, column=0, columnspan=2)
  
# Add an order to the database
def add_order(product, quantity, amount, phone, address):
  cursor = conn.cursor()
  query = "INSERT INTO orders (ProductName, Quantity, Amount, PhoneNumber, DeliveryAddress, DeliveryDate, DeliveryStatus) VALUES (%s, %s, %s, %s, %s, NOW(), 'Processing')"
  cursor.execute(query, (product, quantity, amount, phone, address))
  conn.commit()
  cursor.close()
  print("Order added")

# Create the "Update Status" window
def update_status_window():
  update_window = tk.Toplevel(root)
  update_window.title("Update Status")
  
  # Create the fields for order ID, delivery status, and delivery date
  order_id_label = tk.Label(update_window, text="Order ID")
  order_id_entry = tk.Entry(update_window)
  status_label = tk.Label(update_window, text="Delivery Status")
  status_entry = tk.Entry(update_window)
  date_label = tk.Label(update_window, text="Delivery Date")
  date_entry = tk.Entry(update_window)
  
  # Create the button to update the status in the database
  update_button = tk.Button(update_window, text="Update", command=lambda: update_status(order_id_entry.get(), status_entry.get(), date_entry.get()))
  
  # Place the fields and button in the window
  order_id_label.grid(row=0, column=0)
  order_id_entry.grid(row=0, column=1)
  status_label.grid(row=1, column=0)
  status_entry.grid(row=1, column=1)
  date_label.grid(row=2, column=0)
  date_entry.grid(row=2, column=1)
  update_button.grid(row=3, column=0, columnspan=2)
  
# Update the delivery status in the database
def update_status(order_id, status, date):
  cursor = conn.cursor()
  query = "UPDATE orders SET DeliveryStatus = %s, DeliveryDate = %s WHERE OrderID = %s"
  cursor.execute(query, (status, date, order_id))
  conn.commit()
  cursor.close()
  print("Status updated")

# Create the buttons to choose which window to open
add_button = tk.Button(root, text="Add Order", command=add_order_window)
update_button = tk.Button(root, text="Update Status", command=update_status_window)

# Place the buttons in the main window
add_button.pack()
update_button.pack()

# Start the GUI
root.mainloop()
