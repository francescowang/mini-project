import core
import connectdb
from tabulate import tabulate # if you do it this way, no need to type tabulate.tabulate


# product menu
def product_menu():
    file = open("../data/productmenu.txt", "r")
    productmenu = file.read()
    print(productmenu)
    file.close()


# adding a product
def product_add(product_list):
    core.function_clear()
    product_view(product_list)
    adding_product = input("\nPress Enter to return to Product Menu. What product would you like to add? ").strip()
    if adding_product == "":
        return
    if (any(char.isdigit() for char in adding_product)):
        print(f"\nSorry but {adding_product} is invalid. Please only enter alphabetical characters.\n")
        return
        
    try:
        adding_price = input(f"\nPress Enter to return to Product Menu. What is the price of {adding_product}? ").strip()
        if adding_price == "":
            print("\n")
            return
        adding_price = float(adding_price) # casting it to a float
    except ValueError:
        print(f"\nSorry but {adding_price} is invalid, please input a valid price.\n")
    else:
        print(f"\n{adding_product.title()} has been added to the list of products.\n")
        # input("Press Enter to continue browsing in the Data Cafe app.\n")
        
        add_sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)" # SQL data persistence, in earlier versionm I used txt, csv
        add_value = (adding_product.title().strip(), adding_price) # add .title() here so it capitalises the word to the database
        connectdb.cursor.execute(add_sql, add_value)
        connectdb.connection.commit() # sends changes to the database


# updating a product
def product_update(product_list):
    core.function_clear()
    product_view(product_list)
    try:
        enter_p_id = input("\nPress Enter to return to Product Menu. Please enter an ID to update the product: ").strip()
        if enter_p_id == "": 
            return
        enter_p_id = int(enter_p_id)
    except ValueError:
        print(f"\nSorry but {enter_p_id} is invalid, please input a valid Product ID.\n")
        return
        
    p_name = input("\nPress Enter to return to Product Menu. What is the new product's name? ").strip()
    if p_name.strip() == "":
        return
    if (any(char.isdigit() for char in p_name)):
        print(f"\nSorry but {p_name} is invalid. Please only enter alphaphetical characters.\n")
        return
    
    current_product = search(enter_p_id, product_list)
    try:
        p_price = input(f"\nPress Enter to return to Product Menu. What is the price of {p_name}? ").strip()
        if p_price == "":
            return
        p_price = float(p_price)
    except ValueError:
        print(f"\nSorry but {p_price} is invalid, please input a valid price.\n")
        return
    print(f"\n{p_name.title()} has now replaced the previous product successfully.\n")
    
    update_sql = "UPDATE products SET product_name = %s, price = %s WHERE product_id = %s" # SQL data persistence, in earlier versionm I used txt, csv
    update_value = (p_name.title(), p_price, enter_p_id)
    connectdb.cursor.execute(update_sql, update_value)
    connectdb.connection.commit()


# deleting a product
def product_delete(product_list):
    core.function_clear()
    product_view(product_list)
    try:
        p_delete = input("\nPress Enter to return to Product Menu. Please enter an ID to delete the product: ")
        if p_delete == "":
            return
        p_delete = int(p_delete)
    except ValueError:
        print(f"\nSorry but {p_delete} is invalid, please input a valid Product ID.\n")
        return
    print(f"\nProduct ID {p_delete} has been deleted from the list of products.\n")
    
    delete_sql = "DELETE FROM products WHERE product_id = %s" # SQL data persistence, in earlier versionm I used txt, csv
    delete_value = (p_delete)
    connectdb.cursor.execute(delete_sql, delete_value)
    connectdb.connection.commit()


# printing the product list
def product_view(product_list):
    core.function_clear()
    view_sql = "SELECT * FROM products" # SQL data persistence, in earlier versionm I used txt, csv
    connectdb.cursor.execute(view_sql)
    product_list = connectdb.cursor.fetchall()
    print(tabulate(product_list, headers=["Product ID", "Product Name", "Price £"], tablefmt="fancy_grid"))
    print("\n")


# searching through the product id
def search(product_id, product_list):
    for item in product_list:
        if item["id"] == id:
            return item