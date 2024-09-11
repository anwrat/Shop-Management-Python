import mysql.connector

class Database:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shop_management"
        )
        self.cursor=self.conn.cursor()
    
    def execute_query(self,query,params=None):
        self.cursor.execute(query,params or ())
        self.conn.commit()
    
    def fetch_all(self,query,params=None):
        self.cursor.execute(query,params or ())
        return self.cursor.fetchall()

    def fetch_one(self,query,params=None):
        self.cursor.execute(query,params or ())
        return self.cursor.fetchone()

class Shop:
    def __init__(self):
        self.db=Database()
    
    def add_item_to_inventory(self,name,price,stock):
        query="INSERT INTO items (name,price,stock) VALUES (%s,%s,%s)"
        self.db.execute_query(query,(name,price,stock))
        print(f"Item '{name}' added to inventory")
        
    def sell_item(self,name,quantity):
        item_query="SELECT id,price,stock from items where name =%s"
        item=self.db.fetch_one(item_query,(name,))

        if item:
            item_id,price,stock=item
            if stock>=quantity:
                total_price=price*quantity
                new_stock=stock-quantity
                update_query="UPDATE items SET stock=%s WHERE id=%s"
                self.db.execute_query(update_query,(new_stock,item_id))
                sales_query="INSERT INTO sales(item_id,items_quantity,total_price)VALUE(%s,%s,%s)"
                self.db.execute_query(sales_query,(item_id,quantity,total_price))
                return f"Sold {quantity} of '{name}'. Total Price: {total_price:2f}"
            else:
                return f"Not enough stock for '{name}'."
        else:
            return f"Item '{name}' does not exist in inventory"

    def view_sales_report(self):
        sales_report_query="""SELECT items.name,sales.items_quantity,sales.total_price FROM sales JOIN items ON sales.item_id=items.id"""
        sales=self.db.fetch_all(sales_report_query)
        sales_report=[]
        total_revenue=0
        for sale in sales:
            item_name,quantity,total_price=sale
            sales_report.append(f"Item:{item_name},Quantity:{quantity},Total Price: ${total_price}")
            total_revenue+=total_price
        
        sales_report.append(f"\nTotal Revenue: ${total_revenue:2f}")
        return"\n".join(sales_report)
    
    def display_inventory(self):
        inventory_query="SELECT name,price,stock FROM items"
        inventory=self.db.fetch_all(inventory_query)
        inventory_list=[]
        for item in inventory:
            name,price,stock=item
            inventory_list.append(f"Name:{name},Price:${price:2f},Stock:{stock}")
        return "\n".join(inventory_list)

if __name__=="__main__":
    shop=Shop()
    shop.sell_item("Orange",10)
    print(shop.view_sales_report())
    print(shop.display_inventory()) 