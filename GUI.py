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
    name = name_entry2.get() 
    quantity = int(quantity_entry.get())  
    result = shop.sell_item(name, quantity)
    result_text.insert(END, f"{result}\n")

def view_sales_report():
    result_text.delete("1.0","end")
    result=shop.view_sales_report()
    result_text.insert(END,f"{result}\n")

def show_inventory():
    result_text.delete("1.0","end")
    result=shop.display_inventory()
    result_text.insert(END,f"{result}\n")
root = Tk()
root.title("Shop Management System")

# Create a new style for the button
style = ttk.Style(root)
style.theme_use("default")  # Use 'default' theme for better control
style.configure(
    "Custom.TButton",
    background="green",  # Button background color
    foreground="white",  # Text color
    font=("Helvetica", 10, "bold"),
    borderwidth=1,
    focusthickness=3,
    focuscolor="none",
)
style.map(
    "Custom.TButton",
    background=[("active", "#45a049")],  # Active (hover) state color
    foreground=[("disabled", "gray")],  # Foreground color when disabled
)

#For Quit Button
style2 = ttk.Style(root)
style2.theme_use("default")  # Use 'default' theme for better control
style2.configure(
    "Custom2.TButton",
    background="red",  # Button background color
    foreground="white",  # Text color
    font=("Helvetica", 10, "bold"),
    borderwidth=1,
    focusthickness=3,
    focuscolor="none",
)
style2.map(
    "Custom2.TButton",
    background=[("active", "#6e0902")],  # Active (hover) state color
    foreground=[("disabled", "gray")],  # Foreground color when disabled
)

#Section 1
frm = ttk.Frame(root, padding=20)
frm.grid()

ttk.Label(frm, text="Add Item to Inventory",font=('Times New Roman',20,'bold')).grid(column=0, row=0, columnspan=2,pady=(0,20)) #For space between two widgets or padding, use pady
ttk.Label(frm, text="Name of Item").grid(column=0, row=1,pady=(0,10))
name_entry = ttk.Entry(frm)
name_entry.grid(column=1, row=1,pady=(0,10))

ttk.Label(frm, text="Price").grid(column=0, row=2,pady=(0,10))
price_entry = ttk.Entry(frm)
price_entry.grid(column=1, row=2,pady=(0,10))

ttk.Label(frm, text="Stock").grid(column=0, row=3,pady=(0,20))
stock_entry = ttk.Entry(frm)
stock_entry.grid(column=1, row=3,pady=(0,20))

#Section 2

frm2 = ttk.Frame(root, padding=20)
frm2.grid(row=0,column=2)

ttk.Label(frm2, text="Sell Item",font=('Times New Roman',20,'bold')).grid(column=0, row=0, columnspan=2,pady=(0,20)) 
ttk.Label(frm2, text="Name of Item").grid(column=0, row=1,pady=(0,10))
name_entry2 = ttk.Entry(frm2)
name_entry2.grid(column=1, row=1,pady=(0,10))

ttk.Label(frm2, text="Quantity").grid(column=0, row=2,pady=(0,10))
quantity_entry = ttk.Entry(frm2)
quantity_entry.grid(column=1, row=2,pady=(0,10))


ttk.Button(frm, text="Add Item", command=add_item, style="Custom.TButton").grid(column=0, row=4, padx=5, pady=5)
ttk.Button(frm2, text="Sell Item", command=sell_item, style="Custom.TButton").grid(column=1, row=4, padx=5, pady=5)


# Results Section
result_frame = LabelFrame(root, text="Output", padx=10, pady=10)
result_frame.grid(column=0, row=2, padx=20, pady=10)

# Text widget for displaying results
result_text = Text(result_frame, height=10, width=50, wrap=WORD)
result_text.grid(row=0, column=0)
result_text.config(state=NORMAL)  # Initially editable

ttk.Button(root, text="View Sales", command=view_sales_report, style="Custom.TButton").grid(column=1, row=3, padx=5, pady=5)
ttk.Button(root, text="Display Inventory", command=show_inventory, style="Custom.TButton").grid(column=2, row=3, padx=5, pady=5)
ttk.Button(root, text="Quit", command=root.destroy,style="Custom2.TButton").grid(column=1, row=4, columnspan=2)

# Start the GUI loop
root.mainloop()
