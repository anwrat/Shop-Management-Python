from tkinter import *
from tkinter import ttk
from shop_management_sys import Shop  

shop = Shop()

# Function to add an item to the inventory
def add_item():
    name = name_entry.get()  # Get the item name from the entry field
    price = float(price_entry.get())  # Get the item price
    stock = int(stock_entry.get())  # Get the stock quantity
    shop.add_item_to_inventory(name, price, stock)
    result_label.config(text=f"Added {name} to inventory")

# Function to sell an item
def sell_item():
    name = name_entry.get()  # Get the item name from the entry field
    quantity = int(quantity_entry.get())  # Get the quantity to sell
    result = shop.sell_item(name, quantity)
    result_label.config(text=result)


root = Tk()
root.title("Shop Management System")
frm = ttk.Frame(root, padding=20)
frm.grid()

# GUI Elements
ttk.Label(frm, text="Shop Management System").grid(column=0, row=0, columnspan=2)
ttk.Label(frm, text="Name").grid(column=0, row=1)
name_entry = ttk.Entry(frm)
name_entry.grid(column=1, row=1)

ttk.Label(frm, text="Price").grid(column=0, row=2)
price_entry = ttk.Entry(frm)
price_entry.grid(column=1, row=2)

ttk.Label(frm, text="Stock").grid(column=0, row=3)
stock_entry = ttk.Entry(frm)
stock_entry.grid(column=1, row=3)

# Buttons
ttk.Button(frm, text="Add Item", command=add_item).grid(column=0, row=4)
ttk.Button(frm, text="Sell Item", command=sell_item).grid(column=1, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5, columnspan=2)

# Label to display results
result_label = ttk.Label(frm, text="")
result_label.grid(column=0, row=6, columnspan=2)

root.mainloop()
