import csv
import os
import ast

def PrintOrder():
    order_list = []

    with open('orders.csv', 'r+', newline= '') as file:

        items_in_list = csv.DictReader(file)

        print("")
        print('  Current Orders:   \n')    

        i = 0
        for row in items_in_list:
            print("Index : "+ str(i),row)
            i += 1
            order_list.append(row)
        print('\n')

    return order_list


########################################################################################


def CreateOrder():
    with open('orders.csv', mode='a+', newline='') as file:
        
        orderList=[]

        fieldnames = ['name', 'address', 'phone','courier','status']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
 
        
        name = str(input('Enter name: '))
        address = str(input('Enter address: '))
        phone = str(input('Enterphone number: '))
        courier = str(input('Please enter Courier Number: '))
                  
        dictToPass ={'name': name,
                    'address': address, 
                    'phone': phone, 
                    'courier': courier,
                    'status': 'Preparing'}      

        #if file is empty, then write header
        if os.stat("orders.csv").st_size == 0:
           writer.writeheader()
           writer.writerow(dictToPass)
        else:
            writer.writerow(dictToPass)


########################################################################################

def UpdateStatusOrder():
    order_list = []

    with open('orders.csv', 'r', newline= '') as file:

        items_in_list = csv.DictReader(file)

        print("")
        print('  Current List:   \n')    

        i = 0
        for row in items_in_list:
            print("Index : "+ str(i),row)
            i += 1
            order_list.append(row)
        print('\n')

    

    IndexInput = int(input("Which delivery status (index) would you like to update: "))
    ChangeStatusInput = input("What would you like to change the delivery status to?: ")      

    #changing the value in the list and assiging to a new dict
    
    order_list[IndexInput]["status"] = ChangeStatusInput

    with open('orders.csv', mode='w', newline='') as file:
        

        fieldnames = ['name', 'address', 'phone','courier','status']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
     

        #if file is empty, then write header
        if os.stat("orders.csv").st_size == 0:
           writer.writeheader()
           writer.writerows(order_list)
        else:
            writer.writerows(order_list)
    
###################################################################################    
    
def UpdateFullOrder():
    order_list = []

    with open('orders.csv', 'r+', newline= '') as file:

        items_in_list = csv.DictReader(file)

        print("")
        print('  Current Orders:   \n')    

        i = 0
        for row in items_in_list:
            print("Index : "+ str(i),row)
            i += 1
            order_list.append(row)
        print('\n')

    IndexInput = int(input("Which order (index) would you like to update: "))

    nameUpdate = str(input("New name to update or leave blank: "))
    addressUpdate = str(input("New address to update or leave blank: "))
    phoneUpdate = str(input("New phone number to update or leave blank: "))
    courierUpdate = str(input("New courier to update or leave blank: "))


    changesBeenMade = False

    while True:
        confirmChange= input("Do you want to make these changes y/n?")
        if confirmChange=="y":
            pass
        else:
            #menureturn("Order Menu")
            break

        if nameUpdate== "":
            pass     
        else:
            order_list[IndexInput]["name"] = nameUpdate
            changes_to_order_made = True

        if addressUpdate =="":
            pass
        else:
            order_list[IndexInput]["address"] = nameUpdate
            changes_to_order_made = True

        if phoneUpdate =="":
            pass
        else:
            order_list[IndexInput]["phone"] = nameUpdate
            changes_to_order_made = True

        if courierUpdate =="":
            pass
        else:
            order_list[IndexInput]["courier"] = nameUpdate
            changes_to_order_made = True    
            
        if changesBeenMade == True:
            changesBeenMade = False
            print("\n\nChange(s) to order succesfully made")
        else:
            print("No changes made to order\n")
        break

    fieldnames = ['name', 'address', 'phone','courier','status']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
    

    if os.stat("orders.csv").st_size == 0:
        writer.writeheader()
        writer.writerows(order_list)
    else:
        writer.writerows(order_list)


################################################################################


def DeleteOrder():
    order_list = []

    #read
    with open('orders.csv', 'r', newline= '') as file:

        items_in_list = csv.DictReader(file)

        print("")
        print('  Current Orders:   \n')    

        i = 0
        for row in items_in_list:
            print("Index : "+ str(i),row)
            i += 1
            order_list.append(row)
    print('\n')
    

    #update
    IndexInput = int(input("Which order (index) would you like to delete: "))

    order_list.pop(IndexInput)


    print("\nYour order has been deleted")

    print(order_list)

    #write

    with open('orders.csv', 'w', newline= '') as file:
        fieldnames = ['name', 'address', 'phone','courier','status']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        


        writer.writeheader()
        writer.writerows(order_list)
    

#PrintOrder()
#CreateOrder()
#UpdateStatusOrder()
#UpdateFullOrder()


DeleteOrder()