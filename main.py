# importing mysql library
from mysql.connector import connect, Error
import sys  # to control exit code


def get_pizza_list():
    sql_select_Query = "SELECT * from PizzaRecipes"

    cursor.execute(sql_select_Query)
    return cursor.fetchall()


# list of enabled commands to show in help menus
possibleCommands = [
    "quit",
    "help",
    "list pizzas",
    "add pizza",
    "search pizza",
    "sort list",
]


def get_command_list():
    print("The following commands are available:")
    for command in possibleCommands:
        print(command)


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

# start a while loop to iterate through commands
while True:
    # converting entered command to lower case
    command = input("Please enter command: ").strip().lower()

    # checking if command is equal to "quit"
    if command == possibleCommands[0]:

        print("Thanks for using, goodbye!")
        sys.exit(0)  # exit as 0

    # checking if command is equal to "help"
    elif command == possibleCommands[1]:
        # printing all supported commands

        print("The following commands are available:")
        for command in possibleCommands:
            print(command)

    # checking if command is equal to "list pizzas"
    elif command == possibleCommands[2]:

        # print a list of pizzas stored
        print("List of Recipes:")
        for row in get_pizza_list():
            print(
                str(row[0])
                + " - "
                + str(row[1])
                + ": "
                + str(row[3])
                + " = "
                + str(row[2])
            )
        print("")

    # checking if command is equal to "add pizza"
    elif command == possibleCommands[3]:
        # taking new pizza name as input
        NewItemName = input("Please enter new Pizza name: ")
        while True:
            try:
                NewItemPrice = float(input("Please enter new Pizza price: "))
                break
            except ValueError:
                print("Please insert a valid number (No currency signs)")
        NewItemDescription = input("Please enter new Pizza Ingredients: ")
        # inserting new pizza into database
        sql = "INSERT INTO PizzaRecipes (pizzaName, PizzaPrice, pizzaIngredients) VALUES (%s, %s, %s)"

        val = (NewItemName, NewItemPrice, NewItemDescription)
        cursor.execute(sql, val)
        connection.commit()
        # retrive updated pizza list

        # printing updated pizza list with for loop
        print("Updated List of Recipes:")
        for row in get_pizza_list():
            print(
                str(row[0])
                + " - "
                + str(row[1])
                + ": "
                + str(row[3])
                + " = "
                + str(row[2])
            )
        print("")

    # checking if command is equal to "search pizza"
    elif command == possibleCommands[4]:
        # taking input for search
        searchKey = input("Type here to search for recipes: ")
        # run an sql query to retrive pizza list like inputted string

        sql = """SELECT * from PizzaRecipes where pizzaName LIKE %s"""

        adr = ("%" + searchKey + "%",)
        cursor.execute(sql, adr)
        records = cursor.fetchall()
        # printing search results
        print("Search result:")
        for row in records:
            print(
                str(row[0])
                + " - "
                + str(row[1])
                + ": "
                + str(row[3])
                + " = "
                + str(row[2])
            )
        print("")

    # checking if command is equal to "sort list"
    elif command == possibleCommands[5]:
        # printing possible sorting options
        print(
            "Please choose sorting type: \n1 - ID Ascending\n2 - ID Descending\n3 - Name Ascending\n4 - Name Descending"
        )
        # taking sort type as input
        while True:
            try:
                sortID = int(
                  input(
                    "Please enter sort type (number): "
                    ).strip().lower()
                    )
                if sortID > 0 and sortID < 5:
                    break
            except ValueError:
                print("Please insert a number 1-4")
        # checking if sort type 1 is chosen

        sorts = {
            1: "PizzaID ASC",
            2: "PizzaID DESC",
            3: "PizzaName ASC",
            4: "PizzaName DESC",
        }

        sql_select_Query = f"SELECT * from PizzaRecipes ORDER BY {sorts[sortID]}"

        # execute and fetch correct query
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        # printing pizza list with for loop
        print("List of available Recipes:")
        for row in records:
            print(
                str(row[0])
                + " - "
                + str(row[1])
                + ": "
                + str(row[3])
                + " = "
                + str(row[2])
            )
        print("")

    # If no valid commands are entered
    else:
        # Error message, for invalid command
        # print all supported commands

        print("Command not found")
        get_command_list()
