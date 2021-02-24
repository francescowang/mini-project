import sys
import product_functions 
import courier_functions
import order_functions
import core
import connectdb


# variables, lists
products = []
couriers = []
orders = []


core.function_clear()
core.welcome_message()
core.data_cafe()
username = input("Enter your username: ")


while True:
    core.function_clear()
    core.print_mainmenu() # main menu
    user_value = input(f"\nHi {username.strip()}. Please select an option: ") 
    core.function_clear()
    if user_value == "0":
        core.thank_you()
        sys.exit(0)


    elif user_value == "1": # product menu
        product_menu = True
        while product_menu == True:
            product_functions.product_menu() # imported function
            p_value = input(f"Hi {username.strip()}. Please select an option: ") 
            core.function_clear()
            if p_value == "0":
                core.thank_you()
                connectdb.close_connection() # the data persists and is committed to the database
                sys.exit(0)
            elif p_value == "1":
                core.function_clear()
                product_functions.product_view(products)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n") # when input, the programme stops until the user inputs something
                core.function_clear() # view list of p, then clearing terminal and back to p menu
            elif p_value == "2":
                core.function_clear()
                product_functions.product_add(products) 
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n") # this can also be added at the end of the function, but I added it here for better user experience because I used f-string
                core.function_clear()
            elif p_value == "3":
                core.function_clear()
                product_functions.product_update(products)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n") # if added in the func and here it first displays it in the func, then here, as func is read above
                core.function_clear()
            elif p_value == "4":
                core.function_clear()
                product_functions.product_delete(products)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif p_value == "5":
                core.products_save(products)
                product_menu = False 
            else:
                print(f"\nSorry {username}. This is an invalid input. Please select another option.\n")


    elif user_value == "2": # courier menu
        courier_menu = True
        while courier_menu == True:
            courier_functions.courier_menu()
            c_value = input(f"Hi {username.strip()}. Please select a courier option: ")
            core.function_clear()
            if c_value == "0": 
                core.thank_you()
                connectdb.close_connection()
                sys.exit(0)
            elif c_value == "1":
                core.function_clear()
                courier_functions.courier_view(couriers)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif c_value == "2":
                core.function_clear()
                courier_functions.courier_add(couriers)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif c_value == "3":
                core.function_clear()
                courier_functions.courier_update(couriers)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif c_value == "4":
                core.function_clear()
                courier_functions.courier_delete(couriers)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif c_value == "5":
                core.couriers_save(couriers)
                courier_menu = False
            else:
                print(f"\nSorry {username}. This is an invalid input. Please select another option.\n")


    elif user_value == "3": # order menu
        order_menu = True
        while order_menu == True:
            order_functions.order_menu()
            o_value = input(f"Hi {username.strip()}. Please select an order option: ")
            core.function_clear()
            if o_value == "0":
                core.thank_you()
                connectdb.close_connection()
                sys.exit(0)
            elif o_value == "1":
                core.function_clear()
                order_functions.order_view(orders)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif o_value == "2":
                core.function_clear()
                order_functions.order_add(orders, couriers, products)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif o_value == "3":
                core.function_clear()
                order_functions.order_update_status(orders)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif o_value == "4":
                core.function_clear()
                order_functions.order_update(orders, couriers, products)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif o_value == "5":
                core.function_clear()
                order_functions.order_delete(orders)
                input(f"\nHi {username}, press Enter to continue browsing in the Data Cafe app.\n")
                core.function_clear()
            elif o_value == "6":
                core.orders_save(orders)
                order_menu = False
            else: 
                print(f"\nSorry {username}. This is an invalid input. Please select another option.\n")