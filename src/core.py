import csv
import os
import time



# cleaning the terminal
def function_clear():
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()


# welcome message
def welcome_message():
    function_clear()
    print('''

≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛

 __          __  _                            _______      _______ _            _____        _           _____       __     _ 
 \ \        / / | |                          |__   __|    |__   __| |          |  __ \      | |         / ____|     / _|   | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___      | |  | |__   ___  | |  | | __ _| |_ __ _  | |     __ _| |_ ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \     | |  | '_ \ / _ \ | |  | |/ _` | __/ _` | | |    / _` |  _/ _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |    | |  | | | |  __/ | |__| | (_| | || (_| | | |___| (_| | ||  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/     |_|  |_| |_|\___| |_____/ \__,_|\__\__,_|  \_____\__,_|_| \___(_)                                                                                                                  


≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛
''')
    time.sleep(4)
    function_clear()
    
# printing layout for username
def data_cafe():
    function_clear()
    print('''
                    ✵☆☆☆☆✪✪✪✪☆☆☆☆The Data Cafe☆☆☆☆✪✪✪✪☆☆☆☆✵                                                                                                                                                                       
≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛

                                (  )   (   )  )
                                ) (   )  (  (
                                ( )  (    ) )
                                _____________
                                <_____________> ___
                                |             |/ _ \            
                                |               | | |
                                |               |_| |
                            ___|             |\___/
                            /    \___________/    \                     
                            \_____________________/                     
                                                                                            

''')

# printing thank you when exiting the app.py
def thank_you():
    file = open("../data/thankyou.txt", "r")
    thankyou = file.read()
    print(thankyou)
    file.close()


# printing the main menu from the data folder
def print_mainmenu():
    function_clear()
    file = open("../data/mainmenu.txt", "r")
    mainmenu = file.read()
    print(mainmenu)
    file.close()


# opens products file and appends stored product names to empty product in app.py
def products_read(product_list):
    with open("../data/products.csv", 'r') as products_file:
        products_csv = csv.DictReader(products_file)
        for product_item in products_csv:
            product_list.append(product_item)


# opens couriers file and appends stored courier names to empty courier in app.py
def couriers_read(courier_list):
    with open("../data/couriers.csv", "r") as couriers_file:
        couriers_csv = csv.DictReader(couriers_file)
        for courier_item in couriers_csv:
            courier_list.append(courier_item) 


# opens orders file and appends stored order names to empty order list in app.py
def orders_read(order_list):
    with open ("../data/orders.csv", "r") as orders_file:
        orders_csv = csv.DictReader(orders_file)
        for order_item in orders_csv:
            order_list.append(order_item)


# overwrites products file 
def products_save(product_list):
    with open('../data/products.csv', 'w') as products_file:
        fieldnames = ["Product_Name", "Price"] # field_names -> product_list[0].keys() : keys are Product and Price
        writer = csv.DictWriter(products_file, fieldnames)
        writer.writeheader()
        writer.writerows(product_list)


# overwrites couriers file 
def couriers_save(courier_list):
    with open('../data/couriers.csv', 'w') as couriers_file:
        fieldnames = ["Courier", "Telephone Number"]
        writer = csv.DictWriter(couriers_file, fieldnames)
        writer.writeheader()
        writer.writerows(courier_list)


# overwrites orders file 
def orders_save(order_list):
    with open('../data/orders.csv', 'w') as orders_file:
        fieldnames = ["Name","Address","Telephone Number","Status","Order Products","Order Courier"]
        writer = csv.DictWriter(orders_file, fieldnames)
        writer.writeheader()
        writer.writerows(order_list)