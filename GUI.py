from tkinter import *
from tkinter import ttk
from shop_management_sys import Shop

shop = Shop()

def add_item():
    name = name_entry.get()  
    price = float(price_entry.get())  
    stock = int(stock_entry.get())  
    shop.add_item_to_inventory(name, price, stock)
    result_text.insert(END, f"Added {name} to inventory\n")

def sell_item():
    name = name_entry.get() 
    quantity = int(quantity_entry.get())  
    result = shop.sell_item(name, quantity)
    result_text.insert(END, f"{result}\n")

def view_sales_report():
    result=shop.view_sales_report()
    result_text.insert(END,f"{result}\n")

root = Tk()
root.title("Shop Management System")

# Main Frame
frm = ttk.Frame(root, padding=20)
frm.grid()

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


ttk.Button(frm, text="Add Item", command=add_item).grid(column=0, row=4)
ttk.Button(frm, text="Sell Item", command=sell_item).grid(column=1, row=4)
ttk.Button(frm, text="View Sales", command=view_sales_report).grid(column=2, row=4)


# Results Section
result_frame = LabelFrame(root, text="Results", padx=10, pady=10)
result_frame.grid(column=0, row=5, padx=20, pady=10)

# Text widget for displaying results
result_text = Text(result_frame, height=10, width=50, wrap=WORD)
result_text.grid(row=0, column=0)
result_text.config(state=NORMAL)  # Initially editable

ttk.Button(root, text="Quit", command=root.destroy).grid(column=0, row=10, columnspan=2)

# Start the GUI loop
root.mainloop()
