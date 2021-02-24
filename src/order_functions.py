import core
import connectdb
from courier_functions import courier_view
from product_functions import product_view
from tabulate import tabulate

# order menu
def order_menu():
    file = open("../data/ordermenu.txt", "r")
    order_menu = file.read()
    print(order_menu)
    file.close()


# adding an order
def order_add(order_list, courier_list, product_list):
    core.function_clear()
    order_view(order_list)
    product_selection = [] # this is where the user adds their products
    cust_name = input("\nPress Enter to return to Order Menu. What is the customer's name? ").title().strip()
    if cust_name == "":
        return
    if (any(char.isdigit() for char in cust_name)):
        print(f"\nSorry but {cust_name} is invalid. Please only enter alphaetical characters.\n")
        return
    cust_address = input("\nPress Enter to return to Order Menu. What is the customer's address? ").title().strip()
    if cust_address == "":
        return
    
    try:
        cust_phone = input("\nPress Enter to return to Order Menu. What is the customer's telephone number? ").strip()
        if cust_phone == "":
            print("\n")
            return
        cust_phone = int(cust_phone)
    except ValueError:
        print(f"\nSorry but {cust_phone} is invalid, please input a valid telephone number.\n")
        return
        
    cust_status = "Preparing"
    enter_p_id = ""
    product_view(product_list) # the user can view all products before adding their products
    while enter_p_id != "0": 
        enter_p_id = input("\nEnter 0 when you finish your order. Please type a Product ID: ")
        product_sql = "SELECT * FROM products WHERE product_id = %s"
        value = (enter_p_id)
        connectdb.cursor.execute(product_sql, value)
        the_product_the_user_selected = connectdb.cursor.fetchall() # why doesn't it print as a dictionary?
        if(len(the_product_the_user_selected) > 0): # if the user entered a valid product ID
            product_selection.append(enter_p_id) # appending ids to product selection
        else:
            (print("\nWe apologise for this inconvenience. We do not have this product in stock."))

    print("\n")
    courier_view(courier_list)
    try:
        courier_order = input("\nPress Enter to return to Order Menu or Input a Courier ID: ") 
        if courier_order == "":
            return
        courier_order = int(courier_order)
    except ValueError:
        print(f"\nSorry but {courier_order} is invalid, please input a valid Courier ID.")
        return

    courier_sql = "SELECT * FROM couriers WHERE courier_id = %s" # we select the courier that we want from couriers and save it to "the_courier_we_want"
    courier_value = (courier_order)
    connectdb.cursor.execute(courier_sql, courier_value)
    the_courier_we_want = connectdb.cursor.fetchall()
    
    if len(the_courier_we_want) != 0: # if courier ID is a valid courier
        add_sql = "INSERT INTO orders (name, address, telephone_number, status, courier_id) VALUES (%s, %s, %s, %s, %s)"
        add_value = (cust_name.title(), cust_address, cust_phone, cust_status, courier_order) # how do I link product_id and courier_id here? I think I already linked it
        connectdb.cursor.execute(add_sql, add_value)
        connectdb.connection.commit()
        
        SQL_statement = "SELECT max(order_id) FROM orders" # This returns the most recently added item - max finds the largest value
        connectdb.cursor.execute(SQL_statement)
        newest_order_id = connectdb.cursor.fetchone()[0] #get the id and save to the newest_order_id variable
        
        add_sql2 = "INSERT INTO order_product (order_id, product_id) VALUES (%s, %s)"
        for item in product_selection:
            add_value2 =(newest_order_id,item)
            connectdb.cursor.execute(add_sql2, add_value2)
            connectdb.connection.commit()

# updating an order status
def order_update_status(order_list):
    core.function_clear()
    order_view(order_list)
    
    update_status = int(input("Enter 0 to cancel. To update an order status, enter the order ID: "))
    if update_status == 0:
        return
    
    orders_stats = ["Preparing", "Ready For Delivery", "Out For Delivery", "Delivered"]
    
    x = ("\n")
    for i, item in enumerate(orders_stats):
        x += (f"Status: {i+1} -> {item} \n")
    print(x, "\n")
    
    user_new_status = int(input("Enter 0 to cancel. Enter one of the following options [1] [2] [3] [4] to update the status: ")) # add error message here
    print("\nOrder updated successfully.\n") # needs work
    if user_new_status == 0:
        return
    
    sql = "UPDATE orders SET status = %s WHERE order_id = %s"
    update_status_value = (orders_stats[user_new_status-1], update_status)
    connectdb.cursor.execute(sql, update_status_value)
    connectdb.connection.commit()


# updating an order
def order_update(order_list, courier_list, product_list):
    core.function_clear()
    order_view(order_list)
    connectdb.cursor.execute("SELECT * FROM orders")
    orders = connectdb.cursor.fetchall()
    
    update_the_order = int(input("Enter 0 to cancel. To update an order, Enter the Order ID: ").strip())
    for order in orders:
        if update_the_order == order[0]:
            user_input_new_name = input("\nPress Enter to skip. What would you like to update the name to? " ).title().strip()
            user_input_new_name != ""
            new_address = input("\nPress Enter to skip. What would you like to update the address to? ").title().strip()
            new_address != ""
            new_number = input("\nPress Enter to skip. What would you like to update the telephone number to?: ").strip()
            new_number != ""

            
            product_selection = []
            enter_product_id = 1
            while enter_product_id != 0:
                connectdb.cursor.execute("SELECT product_id, product_name from products")
                products = connectdb.cursor.fetchall()
                product_view(product_list)
                while True:
                    try:
                        enter_product_id = int(input("Enter 0 to continue. Input the Product ID you wish to order: "))
                        print("\n")
                    except '':
                        break
                    except ValueError:
                        print("Please select a valid Product ID.")
                    else:
                        if enter_product_id != 0:
                            product_selection.append(enter_product_id)
                        break
                    
            connectdb.cursor.execute("SELECT courier_id, courier_name FROM couriers ")
            couriers = connectdb.cursor.fetchall()
            courier_view(courier_list)
            while True:
                try:
                    courier_selection = int(input("Enter 0 to continue. Input the Courier ID you wish to order: "))
                    print("\n")
                except ValueError:
                    print("Please select a valid Courier ID.")
                else:
                    break
            
            if user_input_new_name != "":
                connectdb.cursor.execute(f"UPDATE orders SET name = '{user_input_new_name}' WHERE order_id = {update_the_order}") # need quotation marks for strings, but not for ints when passing values to the database
                connectdb.connection.commit()
            if new_address != "":
                connectdb.cursor.execute(f"UPDATE orders SET address = '{new_address}' WHERE order_id = {update_the_order}")
                connectdb.connection.commit()
            if new_number != "":
                connectdb.cursor.execute(f"UPDATE orders SET telephone_number = '{new_number}' WHERE order_id = {update_the_order}")
                connectdb.connection.commit()
            if len(product_selection) > 0:
                for i in product_selection:
                    sql_statement = "INSERT INTO order_product (order_id, product_id) VALUES (%s, %s)"
                    value = (update_the_order, i) # the i refers to the product_id
                    connectdb.cursor.execute(sql_statement, value)
                    connectdb.connection.commit()
            if courier_selection != 0: 
                connectdb.cursor.execute(f"UPDATE orders SET courier_id = {courier_selection} WHERE order_id = {update_the_order}")
                connectdb.connection.commit()


# deleting an order
def order_delete(order_list):
    core.function_clear()
    order_view(order_list)
    try:
        o_delete = input("Press Enter to return to Order Menu. Please enter an ID to delete the order: ")
        if o_delete.strip() == "":
            return
        o_delete = int(o_delete)
    except ValueError:
        print(f"\nSorry but {o_delete} is invalid, please input a valid Order ID.\n")
        return   
    print(f"\nOrder ID {o_delete} has been deleted from the list of orders.\n")
        
    delete_sql = "DELETE FROM orders WHERE order_id = %s"
    delete_value = (o_delete)
    connectdb.cursor.execute(delete_sql, delete_value)
    connectdb.connection.commit()


# printing the order list
def order_view(order_list):
    core.function_clear()
    view_sql = """
SELECT o.order_id, o.name, o.address, o.telephone_number, o.status, o.courier_id, GROUP_CONCAT(p.product_name SEPARATOR ', ')
FROM orders o
INNER JOIN order_product op on op.order_id = o.order_id
JOIN products p on p.product_id = op.product_id
GROUP BY op.order_id
    """ 
    connectdb.cursor.execute(view_sql)
    order_list = connectdb.cursor.fetchall()
    print("\t\t\t\t ✵✵✵✵☆☆☆☆☆☆☆☆✪✪✪✪☆☆☆☆☆☆☆☆The Data Cafe☆☆☆☆☆☆☆☆✪✪✪✪☆☆☆☆☆☆☆☆✵✵✵✵")
    print(tabulate(order_list, headers=["Order ID", "Customer Name", "Address", "Telephone Number", "Order Status", "Courier ID", "Products Ordered"], tablefmt="fancy_grid"))
    print("\n")