import json;
from prettytable import PrettyTable

# Customer Onboarding function
def customerOnboarding():
    tableNo = input("Enter your table number:\t")
    maxTable = 20;

    while(tableNo != "quit" and tableNo != "q"):
        if(int(tableNo) < 1 or int(tableNo) > maxTable):
            tableNo = input("Table not exists. Try again.\nEnter your table number else enter 'q' or 'quit' to exit:\t")
        else:
            print("Welcome Customer. Your table number is ", tableNo);
            action = input("Enter the action number to continue.\n1. To view carte and order food.\n2. To view the order placed.\nWhat would you like to do?\t");

            while(action != 'q' and action != 'quit'):
                if(action == '1'):
                    customerMenu(tableNo);
                    break;
                elif(action == '2'):
                    customerOrders();
                    break;
                else:
                    action = input("\nInvalid action, try again.\nEnter the action number to continue.\n1. To view carte and order food.\n2. To view the order placed.\nEnter 'q' or 'quit' to exit.\nWhat would you like to do?\t");
            else:
                print("Thank You for visiting. Bis Bald!!")
            break;
    else:
        print("Thank You for visiting. Bis Bald!!")

# Customer Display menu and place order
def customerMenu(tableNo):
    fd = open("menu.json",'r')
    data = fd.read();
    fd.close()

    menu = json.loads(data);

    t = PrettyTable(['Dish UID', 'Dish Name', 'Dish Price (in INR)'])
    for dish in menu:
        t.add_row([dish, menu[dish]['name'],menu[dish]['price']])

    order = input("{}\nNote:Repeat the UID for increasing quantity.\nEnter the UID of the dishes you want to order separated by comma.\t\n".format(t))

    order = order.split(",")
    finalOrder = []

    # Confirm Order Section
    t.clear_rows()
    for uid in order:
        if (menu.get(uid)):
            finalOrder.append(uid)
            t.add_row([uid, menu[uid]['name'],menu[uid]['price']])
        else:
            print("\n{} UID is invalid.".format(uid))

    confirmation = input("\nYour Order:\n{}\nNote: Order once placed cannot be cancelled.\nEnter 'y' to place order or 'c' to cancel.\t".format(t))
    while (confirmation != 'c'):
        if(confirmation == 'y'):
            confirmOrder(tableNo, menu, finalOrder)
            break;
        elif (confirmation == 'c'):
            print("Thank You for visiting. Bis Bald!!")
            break;
        else:
            confirmation = input("Invalid input, try again.\nEnter 'y' to place order or 'c' to cancel.\t")
    else:
        print("Thank You for visiting. Bis Bald!!")

# Confirm Order
def confirmOrder(tableNo, menu, items):
    fd = open("orders.json","r")
    orders = fd.read()
    fd.close();
    orders = json.loads(orders)

    name = input("Enter your name:\t")
    contact = input("Enter your contact number:\t")

    if(len(orders.items()) == 0):
        orders["1"] = {"tableNo":tableNo,"customerName":name, "customerContact":contact, "items":items, "checkedOut":False}
    else:
        for entry in list(orders.values()):
            if(entry['tableNo'] == tableNo and entry['checkedOut'] == 'False'):
                print(key)
                print(entry)
                break;
            elif(entry['tableNo'] == tableNo and entry['checkedOut'] == 'True'):
                continue;
            else:
                print("New Order") 
                break;

# Fetch Order Placed
def customerOrders():
    pass;