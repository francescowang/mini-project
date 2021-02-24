import core
import connectdb
from tabulate import tabulate


# courier menu
def courier_menu():
    file = open("../data/couriermenu.txt", "r")
    couriermenu = file.read()
    print(couriermenu)
    file.close()


# adding a courier
def courier_add(courier_list):
    core.function_clear()
    courier_view(courier_list)
    adding_courier = input("\nPress Enter to return to Courier Menu. What courier would you like to add? ").strip()
    if adding_courier == "": 
        return
    if (any(char.isdigit() for char in adding_courier)):
        print(f"\nSorry but {adding_courier} is invalid. Enter a valid name.\n")
        return
    
    try:
        adding_number = input(f"\nPress Enter to return to Courier Menu. What is {adding_courier}'s telephone number? ").strip()
        if adding_number == "":
            print("\n")
            return
        adding_number = int(adding_number)
    except ValueError:
        print(f"\nSorry but {adding_courier} is invalid, please enter valid a telephone number.\n")
    else:
        print(f"\n{adding_courier.title()} has been added to the list of couriers.\n")
        # input("Press Enter to continue browsing in the Data Cafe app.\n")
        
        add_sql = "INSERT INTO couriers (courier_name, telephone_number) VALUES (%s, %s)"
        add_value = (adding_courier.title(), adding_number)
        connectdb.cursor.execute(add_sql, add_value)
        connectdb.connection.commit()


# updating a courier
def courier_update(courier_list):
    core.function_clear()
    courier_view(courier_list)
    try:
        enter_c_id = input("\nPress Enter to return Courier Menu. Please enter an ID to update the courier: ").strip()
        if enter_c_id == "":
            return
        enter_c_id = int(enter_c_id)
    except ValueError:
        print(f"Sorry but {enter_c_id} is invalid, please input a valid Courier ID.\n")
        return
    
    c_name = input("\nPress Enter to return to Courier Menu. What is new courier's name?: ").strip()
    if c_name.strip() == "":
        return
    if (any(char.isdigit() for char in c_name)):
        print(f"\nSorry but {c_name} is invalid. Please only enter alphabetical characters.")
        return
    
    current_courier = search(enter_c_id, courier_list)
    try:
        c_number = input(f"\nWhat is {c_name}'s telephone number? ").strip()
        if c_name == "":
            return
        c_number = int(c_number)
    except ValueError:
        print(f"\nSorry but {c_number} is invalid, please input a valid telephone number.\n")
        return
    print(f"\n{c_name.title()} has now replaced the previous courier successfully.\n")
    
    update_sql = "UPDATE couriers SET courier_name = %s, telephone_number = %s WHERE courier_id = %s"
    update_value = (c_name, c_number, enter_c_id)
    connectdb.cursor.execute(update_sql, update_value)
    connectdb.connection.commit()


# deleting a courier
def courier_delete(courier_list):
    core.function_clear()
    courier_view(courier_list)
    try:
        c_delete = input("\nPress Enter to return to Courier Menu. Please enter an ID to delete the courier: ")
        if c_delete == "":
            return
        c_delete = int(c_delete)
    except ValueError:
        print(f"\nSorry but {c_delete} is invalid, please input a valid Courier ID.\n")
        return
    print(f"\nCourier ID {c_delete} has been deleted from the list of couriers.\n")
        
    delete_sql = "DELETE FROM couriers WHERE courier_id = %s"
    delete_value = (c_delete)
    connectdb.cursor.execute(delete_sql, delete_value)
    connectdb.connection.commit()


# printing the courier list
def courier_view(courier_list):
    core.function_clear()
    view_sql = "SELECT * FROM couriers" # use `` back quotation marks if you have space
    connectdb.cursor.execute(view_sql)
    courier_list = connectdb.cursor.fetchall()
    print(tabulate(courier_list, headers=["Courier ID", "Courier Name", "Telephone Number"], tablefmt="fancy_grid"))
    print("\n")


# searching through the courier id
def search(courier_id, courier_list):
    for courier in courier_list:
        if courier["id"] == id:
            return courier