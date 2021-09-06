import json
shop=open("shoprecored.json","r")
sale=open("sales.json","r")
shop_data=shop.read()
sale_data=sale.read()
record = json.loads(shop_data)
record_sale=json.loads(sale_data)
shop.close()
sale.close()

def check_inventory_item():
    print("\n\n")
    Item_ID = input("Enter Item ID: ")
    if Item_ID in record.keys():
        print(f"Yes!! {Item_ID} is present")
        print(f"Product ID: {Item_ID}")
        print(f"Product Name: " ,record[Item_ID]["Item Name"])
        print(f"Price: " ,record[Item_ID]["Price"])
        print(f"Quantity: " ,record[Item_ID]["Quantity"])
    else:
        print(f"No!! {Item_ID} is not present")


def update_item_inventory():
    print("\n\n")
    Item_ID = input("Enter Item ID: ")
    if Item_ID in record.keys():
        print(f"Product ID: {Item_ID}")
        print(f"Product Name: " ,record[Item_ID]["Item Name"])
        print(f"Price: " ,record[Item_ID]["Price"])
        print(f"Quantity: " ,record[Item_ID]["Quantity"])
        change=int(input("\nPress:\n1. Update Price:\n2.Update Quantity: "))
        if change==1:
            pr=int(input("Enter updated Price: "))
            record[Item_ID] = {"Item Name": record[Item_ID]["Item Name"], "Quantity": record[Item_ID]["Quantity"], "Price": pr, "Weight": record[Item_ID]["Weight"], "Category": record[Item_ID]["Category"], "Brand": record[Item_ID]["Brand"] }
            update_inventory()
        elif change==2:
            qn=int(input("Enter updated Quantity: "))
            record[Item_ID] = {"Item Name": record[Item_ID]["Item Name"], "Quantity": qn, "Price": record[Item_ID]["Price"], "Weight": record[Item_ID]["Weight"], "Category": record[Item_ID]["Category"], "Brand": record[Item_ID]["Brand"] }
            update_inventory()
        else:
            print("Invalid option selected")

    else:
        print(f"No!! {Item_ID} is not present")

def check_sales_item():
    print("\n\n")
    count=0
    mob = input("Enter Mobile No: ")
    for m_key in record_sale:
        if(record_sale[m_key]['Mobile']==mob):
            count=1

    if count==1:
        print(f"Customer ID: " ,m_key)
        print(f"Mobile: " ,record_sale[m_key]["Mobile"])
        print(f"Product Name: " ,record_sale[m_key]["Customer_Name"])
        print(f"Mobile: " ,record_sale[m_key]["Mobile"])
    else:
        print(f"No customer with {mob} exists")
        

def add_data():
    print("\n\n")
    Item_ID = input("Enter Item ID: ")
    Item_Name = input("Enter Item Name: ")
    qn = int(input("Enter Quantity: "))
    pr = int(input("Enter Price: "))
    w = input("Enter Weight: ")
    cate = input("Enter Category: ")
    brand = input("Enter Brand: ")
    record[Item_ID] = {"Item Name": Item_Name, "Quantity": qn, "Price": pr, "Weight": w, "Category": cate, "Brand": brand }
    update_inventory()

def  check_inventory():
    print(record)

def  check_sales():
    print(record_sale)

def purchase():
    print("\n\n")
    name=input("Your name please: ") 
    phone=input("Your number please: ")
    Item_ID = input("Enter Item ID: ")

    if Item_ID in record.keys():
        qn = int(input("Enter Quantity: "))
        if qn<=int(record[Item_ID]["Quantity"]):
            print(f"Product ID: {Item_ID}")
            print(f"Product Name: " ,record[Item_ID]["Item Name"])
            print(f"Price: " ,record[Item_ID]["Price"])
            print(f"Total Amount: " ,record[Item_ID]["Price"]*qn)

            record[Item_ID]["Quantity"]=record[Item_ID]["Quantity"] - qn
            #print(f"Updated Quantity " ,record[Item_ID]["Quantity"])
            update_inventory()
        
            record_sale[len(record_sale)+1] = {"Customer_Name": name, "Mobile": phone, "Item ID": Item_ID, "Quantity": qn, "Total_amount": record[Item_ID]["Price"]*qn }
            update_sales()
        else:
            print("Not that amount of item in stock")
    else:
        print(f"No item with {Item_ID} exists")


def update_inventory():
    js = json.dumps(record)
    fd = open("shoprecored.json",'w')
    fd.write(js)
    fd.close()

def update_sales():
    js = json.dumps(record_sale)
    fd1 = open("sales.json",'w')
    fd1.write(js)
    fd1.close()


print("\n\n                     Welcome to Inventary Management System\n\n")
c=1
while(c==1):
    print("\n\n                                 MAIN MENU\n\n")
    switch=int(input("Press:\n1. Check Inventary record\n2. Check Sales record\n3. Add item in inventory\n4. Make an Purchase\n5. Check Inventary Item\n6. Check Customer details\n7. Update Inventary Item\n8. Exit:    "))
    if(switch==1):
        check_inventory()
    elif switch==2:
        check_sales()
    elif switch==3:
        add_data()
    elif switch==4:
        purchase()
    elif switch==5:
        check_inventory_item()
    elif switch == 6:
        check_sales_item()
    elif switch ==7:
        update_item_inventory()
    elif switch == 8:
        c=0
    else:
        ("Undefined Input")