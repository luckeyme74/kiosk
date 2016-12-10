def find_customer(customer):
    with open("CustomerList.txt", "r") as r:
            customer_list = r.readlines()
            for item in customer_list:
                record = item.split(",")
                if customer == record[0]:
                    return record
    return "none"

def returning():
    my_customer = get_customer()
    customer_record = find_customer(my_customer)
    if customer_record == "none":
        print ("That number was not found. Try again.")
        returning()
    else:
        for item in customer_record:
            print item

def guest():
    if entry == 3:
        print ("Welcome! We hope to see you often!")

def new():
    try:
        custfile = open("CustomerList.txt", "r+")
        custlist = list(custfile)
        fileindex = len(custlist)
        custfile.close()
        print ("Please enter the following information to generate your customer I.D.\n")
        print ("\n")
        new_first = raw_input("First name:\n")
        new_last = raw_input("Last name:\n")
        new_street = raw_input("Address:\n")
        new_city = raw_input("City:\n")
        new_state = raw_input("State:\n")
        new_zip = raw_input("Zip Code:\n")
        new_phone = raw_input("Last four digits of your phone number:\n")
        str_phone = str(fileindex+1)+ new_phone
        print ("\n")
        print ("Your customer I.D. is being generated...\n")
        new_cust = str_phone + ", " + new_first + " " + new_last + ", " + new_street + ", " + new_city + ", " + new_state + " " + new_zip + "\n"
        print (new_cust)
        custfile = open("CustomerList.txt", "a+")
        custfile.write(new_cust)
        custfile.close()
        print ("Welcome, " + new_first + "! Your customer I.D. is " + str_phone)
    except:
        print ("File Not Found")






def get_customer():
    customer = raw_input("Please enter your customer number:  \n")
    return customer


entry = 0
if entry >=0:
    print (">*< >*< >*< >*< >*< >*< >*<")
    print (" Please choose an option:\n")
    print ("1. Returning Customer")
    print ("2. New Customer")
    print ("3. Guest")
    print (">*< >*< >*< >*< >*< >*< >*<")
    entry = int(raw_input("Enter option:     "))
    if entry < 1 or entry > 3:
        entry = int(raw_input("Please enter Customer option 1, 2 or 3:     "))
    elif entry == 1:
        returning()
    elif entry == 2:
        new()
    elif entry == 3:
        guest()

