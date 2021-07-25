# LOOK FOR "ACTIVITY HERE" COMMENTS


# importing mysql library
from mysql.connector import connect, Error

# establishing connection to mysql database with try catch statement
try:
    connection = connect(
        host="pythonactivities.cotpafanc2of.eu-west-2.rds.amazonaws.com",
        user="admin",
        password="admin1234",
        database="PythonActivities",
    )
except Error as e:
    print(e)

# initailising all variables
cursor = connection.cursor()

# ACTIVITY HERE
# fill list below with all possible commands. look at the functions in the while loop to get index of each command
possibleCommands = []

# starting a while loop to iterate through commands
while True:
    # converting entered command to lower case
    command = input("Please enter command: ").strip().lower()

    # checking if command is equal to "quit"
    if command == possibleCommands[2]:
        # Displaying "bye" message and closing program

        # ACTIVITY HERE
        # print goodbye message

        print("")
        exit()

    # checking if command is equal to "help"
    elif command == possibleCommands[0]:
        # printing all supported commands

        # ACTIVITY HERE
        # write print statement to print all possible commands (find the possibleCommands variable)

        print("")

    # checking if command is equal to "list pizzas"
    elif command == possibleCommands[3]:
        # running sql query to retrive pizza list

        # ACTIVITY HERE
        # Please insert list pizza (select) sql command here
        sql_select_Query = ""

        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        # printing pizza list with for loop
        print("List of Recipes:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # checking if command is equal to "add pizza"
    elif command == possibleCommands[1]:
        # taking new pizza name as input
        NewItemName = input("Please enter new Pizza name: ")
        NewItemPrice = input("Please enter new Pizza price: ")
        NewItemDescription = input("Please enter new Pizza Ingredients: ")
        # inserting new pizza into database
        
        # ACTIVITY HERE
        # Please insert add pizza (insert) sql command here
        sql = ""

        val = ("NULL", NewItemName, NewItemPrice, NewItemDescription)
        cursor.execute(sql, val)
        connection.commit()
        # running sql query to retrive updated pizza list

        # ACTIVITY HERE
        # Please insert list pizza (select) sql command here
        sql_select_Query = ""

        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # printing updated pizza list with for loop
        print("Updated List of Recipes:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # checking if command is equal to "search pizza"
    elif command == possibleCommands[4]:
        # taking input for search
        searchKey = input("Type here to search for recipes: ")
        # running sql query to retrive pizza list where pizza name is like entered string

        # ACTIVITY HERE
        # Please insert search pizza (select and with) sql command here. we have already added 3 quotations on each side to deal with sql injection, please enter your command in between
        sql = """"""

        adr = ("%"+searchKey+"%", )
        cursor.execute(sql, adr)
        records = cursor.fetchall()
        # printing search results
        print("Search result:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")
    
    # checking if command is equal to "sort list"
    elif command == possibleCommands[5]:
        # printing possible sorting options
        print("Please choose sorting type: \n1 - ID Ascending\n2 - ID Descending\n3 - Name Ascending\n4 - Name Descending")
        # taking sort type as input
        sortID = input("Please enter sort type (number): ").strip().lower()
        # checking if sort type 1 is chosen
        if sortID == "1":
            # running sql query to retrive sorted pizza list

            # ACTIVITY HERE
            # Please insert order pizza (select and orderby) sql command here (this is for ID Ascending)
            sql_select_Query = ""


            cursor.execute(sql_select_Query)
        # checking if sort type 2 is chosen
        if sortID == "2":
            # running sql query to retrive sorted pizza list

            # ACTIVITY HERE
            # Please insert order pizza (select, orderby and desc) sql command here (this is for ID Descending)
            sql_select_Query = ""

            cursor.execute(sql_select_Query)
        # checking if sort type 3 is chosen
        if sortID == "3":
            # running sql query to retrive sorted pizza list

            # ACTIVITY HERE
            # Please insert order pizza (select and orderby) sql command here (this is for Name Ascending)
            sql_select_Query = ""

            cursor.execute(sql_select_Query)
        # checking if sort type 4 is chosen
        if sortID == "4":
            # running sql query to retrive sorted pizza list

            # ACTIVITY HERE
            # Please insert order pizza (select, orderby and desc) sql command here (this is for Name Descending)
            sql_select_Query = ""

            cursor.execute(sql_select_Query)
        # fetching queried data
        records = cursor.fetchall()
        # printing pizza list with for loop
        print("List of available Recipes:")
        for row in records:
            print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
        print("")

    # If no valid commands are entered
    else:
        # Error message, for invalid command
        # printing all supported commands

        # ACTIVITY HERE
        # print error message here and all possible commands (use seperate print statements)

        print("")