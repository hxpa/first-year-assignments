# Patel Assignment 1 Program
import _sqlite3 as sqlite  # import sqlite
import pandas as pd  # import pandas library

conn = sqlite.connect('assignment1.db')  # create global variable that connects to database
c = conn.cursor()  # creates global variable that creates a cursor to the database


def startup():  # use a function for different parts of the program to make it easier to understand and debug
    print("Hello and welcome to ClothingBrand1's new interactive software!")
    print("What type of user are you?")
    print("Press 1 if you are USER.")
    print("Press 2 if you are ADMIN.")
    print("Press 3 if you are SALES STAFF.")
    user_input_startup = int(input())  # uses user input to determine what they would like to do
    if user_input_startup == 1:  # standard if statement
        print(user())  # prints specific function based on user input
    elif user_input_startup == 2:
        print(admin())
    elif user_input_startup == 3:
        print(sales_staff())
    else:  # prints error message if user does not fulfil criteria
        print("You have not inputted a valid number, please try again.")
        print(startup())  # reruns the function- allows user to try again


def user():
    print("What would you like to do today?")
    print("Press 1 if you would like to search for an item.")  # complete
    print("Press 2 if you would like to purchase items.")  # complete
    print("Press 3 if you would like to view items.")  # complete
    print("Press 4 if you would like to view an old transaction.")  # complete
    print("Press 5 if you would like to return items.")  # complete
    user_input_user = int(input())
    if user_input_user == 1:
        search_id = input("Please enter the unique ID of the item you would like to search for: ")  # user input
        c.execute("SELECT * FROM Items WHERE id = ?", search_id)  # selects the specific row of database that matches /
        # the user input (variable search_id)
        print(c.fetchall())  # prints this on the screen
    elif user_input_user == 2:
        print(user_input_2())  # once again use function to create easier to understand code and debugging
    elif user_input_user == 3:
        print("These are the available items:")
        print(pd.read_sql_query("SELECT * FROM Items", conn))  # prints the entire table of database called Items
    elif user_input_user == 4:
        print("These are the old transactions:")
        print(pd.read_sql_query("SELECT * FROM Receipt", conn))  # prints the entire table of database called Receipt
    elif user_input_user == 5:
        print("To remove an item follow the steps to delete your purchase from the database and add it back into /"
              "available stock.")
        print("Remove purchase from the database: ")
        receipt_id = input("Please enter the unique receipt ID of the item you would like to return: ")
        delete_receipt = (
            "DELETE FROM Receipt WHERE receipt_id = ?")  # deletes row that has id user inputted
        conn.execute(delete_receipt, receipt_id)  # executes the two variables
        conn.commit()
        print("Thank you very much.")
        print("Add back into available stock: ")
        print("You will need the unique ID of the item and the current number of stock.")
        id_item = input("Please enter the unique ID of the item you would like to return: ")
        edit_stock = input("Please enter the new stock of the item (Just add one to current stock number: ")
        edit_item = '''UPDATE Items
        SET stock = ?
        WHERE id = ?'''  # updates the stock column of Items that has id user inputted by value user inputted

        conn.execute(edit_item,
                     (edit_stock, id_item))  # executes variables
        conn.commit()
        print("Thank you very much. Item has been returned successfully.")
    else:
        print("You have not inputted a valid number, please try again.")
        print(user())  # allows the user to try again (reruns the function)


def user_input_2():
    print("Please follow the steps to purchase an item.")
    print("Once again, these are the available items:")
    print(pd.read_sql_query("SELECT * FROM Items", conn))  # prints the entire table of database called Items
    receipt_name = input("Please enter the name of the item: ")  # creates variables that users can store info into
    receipt_price = input("Please enter the price of the item: ")
    receipt_date = input("Please enter the current date in DD/MM/YY format: ")

    add_receipt = (  # creates variable that inserts into database
        "INSERT INTO Receipt (item_name, item_price, date) VALUES (?, ?, ?)")  # inserts user inputted values /
    #  into certain fields of table Receipt in database
    conn.execute(add_receipt, (receipt_name, receipt_price, receipt_date))  # executes the variables
    conn.commit()
    print("Thank you very much for your purchase.")
    buy_again = input("Would you like to purchase another item? (1 for yes).")  # creates if statement enables users /
    # to go through process again and buy items
    if buy_again == 1:
        print(user_input_2())
    else:
        print("Thank you for your time!")


def admin():
    print("What would you like to do today?")
    print("Press 1 if you would like to add items.")  # complete
    print("Press 2 if you would like to remove items.")  # complete
    print("Press 3 if you would like to edit items.")  # complete
    print("Press 4 if you would like to review sales data and reports.")  # complete
    print("Press 5 if you would like to view most popular items.")  # complete
    print("Press 6 if you would like to apply discounts.")  # complete
    print("Press 7 if you would like to add sales staff.")  # complete
    print("Press 8 if you would like to remove sales staff.")  # complete
    user_input_admin = int(input())
    if user_input_admin == 1:
        print("Please follow the steps to add an item:")
        name = input("Please enter the name of the item: ")  # creates variables that users can store info into
        price = input("Please enter the price of the item (not inc currency): ")
        stock = input("Please enter the item stock: ")

        add_item = (  # creates variable that inserts into database
            "INSERT INTO Items (name, price, stock) VALUES (?,?,?)")  # inserts user inputted values into certain /
    # fields of table Items in database
        conn.execute(add_item, (name, price, stock))  # executes the variables
        conn.commit()
        print("Thank you very much. " + name + " has been added.")
    elif user_input_admin == 2:
        print("Please follow the steps to remove an item:")
        user_id = input("Please enter the unique ID of the item you would like to delete: ")  # allows users to input /
        # id of item wanted to be deleted
        delete_item = (  # variable that deletes row in database
            "DELETE FROM Items WHERE id = ?")  # deletes row that has id user inputted
        conn.execute(delete_item, user_id)  # executes variables
        conn.commit()
        print("Thank you very much. Item with id: " + user_id + " has been deleted.")
    elif user_input_admin == 3:
        print("Please follow the steps to edit an item:")
        id_item = input("Please enter the unique ID of the item you would like to edit: ")  # allows users to input id /
        # of item wanted to be edited
        edit_name = input("Please enter the new name of the item: ")  # creates variable that stores user input
        edit_price = input("Please enter the new price of the item: ")
        edit_stock = input("Please enter the new stock of the item: ")
        edit_item = '''UPDATE Items 
        SET name = ?,
        price = ?,
        stock = ?
        WHERE id = ?'''  # creates variable that updates rows in Items table by ?

        conn.execute(edit_item,
                     (edit_name, edit_price, edit_stock, id_item))  # all variables called (tells program values of /
        # ? as variable names)
        conn.commit()
        print("Thank you very much. The item with the unique ID: " + id_item + "has been edited.")
    elif user_input_admin == 4:
        print("These are the current sales data and reports:")
        print("The table below consists of every purchase made: ")
        print(pd.read_sql_query("SELECT * FROM Receipt", conn))  # prints the entire table of database called Receipt
        print("The table below consists of every invoice made: ")
        print(pd.read_sql_query("SELECT * FROM Invoice", conn))  # prints the entire table of database called invoice
        print("The table below shows the remaining stock of each item: ")
        print(pd.read_sql_query("SELECT * FROM Items ORDER BY stock", conn))  # prints the column of table Items but /
        # orders it from highest to lowest
    elif user_input_admin == 5:
        print("The table below shows the most popular items:")
        print(pd.read_sql_query("SELECT * FROM Items ORDER BY stock", conn))  # prints the column stock of table Items /
        # but orders it from highest to lowest
    elif user_input_admin == 6:
        print("Please follow the steps to apply discounts to an item:")
        id_discount = input("Please enter the unique ID of the item you would like to edit: ")  # stores user input /
        # into variables
        discount_price = input("Please enter the new price of the item: ")
        discount_item = '''UPDATE Items
        SET price = ?
        WHERE id = ?'''  # creates variable that updates price in Items table by ?

        conn.execute(discount_item,
                     (discount_price, id_discount))  # all var called (tells program values of ? as var names)
        conn.commit()
        print("Thank you very much. The item with the unique ID: " + id_discount + "has been edited.")
    elif user_input_admin == 7:
        print("Please follow the steps to add sales staff:")
        staff_name = input("Please enter the name of staff member: ")  # stores user input into variables
        staff_age = input("Please enter the age of staff member: ")

        add_staff = (  # creates variable that inserts into Staff table of database
            "INSERT INTO Staff (staff_name, staff_age) VALUES (?, ?)")  # inserts into specific columns by values of ?
        conn.execute(add_staff, (staff_name, staff_age))  # sets ? as variables created previously
        conn.commit()
        print("Thank you very much. " + staff_name + " has been added to sales staff.")
    elif user_input_admin == 8:
        print("Please follow the steps to remove sales staff:")
        staff_id = input("Please enter the unique ID of the staff member you would like to delete: ")  # allows users /
        # to input id and program stores this in variable
        delete_staff = (  # creates variable that deletes rows in Staff table of database
            "DELETE FROM Staff WHERE staff_id = ?")  # deletes specific rows that have value of ?
        conn.execute(delete_staff, staff_id)  # sets value ? as variable created previously
        conn.commit()
        print("Thank you very much. Sales staff member with id: " + staff_id + " has been deleted.")
    else:
        print("You have not inputted a valid number, please try again.")
        print(admin())  # reruns function to allow users to try again upon fail


def sales_staff():
    print("What would you like to do today?")
    print("Press 1 if you would like to view inventory.")  # complete
    print("Press 2 if you would like to make an invoice")  # complete
    print("Press 3 if you would like to return items.")  # complete
    user_input_sales_staff = int(input())
    if user_input_sales_staff == 1:
        print(pd.read_sql_query("SELECT * FROM Items", conn))  # prints the entire table of database called Items
    elif user_input_sales_staff == 2:
        print("Please follow the steps to create an invoice")
        sales_staff_name = input("Please enter staff member name: ")  # stores user input into variables
        item_name = input("Please enter the item name: ")
        price_invoice = input("Please enter the price of invoice: ")
        time_invoice = input("Please enter the exact time of invoice creation: ")
        date_invoice = input("Please enter the exact date of invoice creation: ")

        add_invoice = (  # creates variable that inserts rows in Invoice table of database
            "INSERT INTO Invoice (sales_staff_name, item_name, price, time, date) VALUES (?, ?, ?, ?, ?)")  # inserts /
        # ? into specific Invoice columns
        conn.execute(add_invoice, (sales_staff_name, item_name, price_invoice, time_invoice, date_invoice))  # defines /
        # ? as variables created previously
        conn.commit()
        print("Thank you. Invoice has been made.")
    elif user_input_sales_staff == 3:
        print("To remove an item follow the steps to delete purchase from the database and add it back into /"
              "available stock.")
        print("Remove purchase from the database: ")
        receipt_id = input("Please enter the unique receipt ID of the item you would like to return: ")  # allows /
        # users to input id of receipt wanted to be deleted
        delete_receipt = (  # creates variable that deletes rows from Receipt table with id ?
            "DELETE FROM Receipt WHERE id = ?")
        conn.execute(delete_receipt, receipt_id)  # sets ? as variable created previously
        conn.commit()
        print("Thank you very much.")
        # this is done as when returning items the receipt of purchase needs to be deleted.
        print("Add back into available stock: ")
        print("You will need the unique ID of the item and the current number of stock.")
        id_item = input("Please enter the unique ID of the item you would like to return: ")  # once again uses user /
        # input and stores in variable
        edit_stock = input("Please enter the new stock of the item (Just add one to current stock number: ")
        edit_item = '''UPDATE Items
         stock = ?
         WHERE id = ?'''  # creates variable that edits the stock column of items table by ?

        conn.execute(edit_item,
                     (edit_stock, id_item))  # sets ? as variable created previously
        conn.commit()
        print("Thank you very much. Item has been returned successfully.")
    else:
        print("You have not inputted a valid number, please try again.")
        print(sales_staff())  # reruns function on user inputting wrong number


print(startup())  # prints the created function startup
