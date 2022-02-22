import csv
import os
import funcs

def PrintOrder():
    order_list= funcs.readCSVFile('db/orders.csv')

########################################################################################


def CreateOrder():
    with open('db/orders.csv', mode='a+', newline='') as file:
        
        orderList=[]

        fieldnames = ['name', 'address', 'phone','courier','status','items']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
 
        
        name = str(input('Enter name: '))
        address = str(input('Enter address: '))
        phone = str(input('Enterphone number: '))
        courier = str(input('Please enter Courier Number: '))

        print("")
        
        order_list= funcs.readCSVFile('db/orders.csv')
        
        new_items= input("Please enter products seperated by comma: ").split(",")
        userNewItems = list(map(int, new_items))

        
        with open('db/orders.csv', mode='a+', newline='') as file:
            
            fieldnames = ['name', 'address', 'phone','courier','status','items']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
                  
            dictToPass ={'name': name,
                        'address': address, 
                        'phone': phone, 
                        'courier': courier,
                        'status': 'Preparing',
                        'items': userNewItems}      

            #if file is empty, then write header
            if os.stat("db/orders.csv").st_size == 0:
                writer.writeheader()
                writer.writerow(dictToPass)
            else:
                writer.writerow(dictToPass)


########################################################################################


def UpdateStatusOrder():
    order_list= funcs.readCSVFile('db/orders.csv')

    IndexInput = int(input("Which delivery status (index) would you like to update: "))
    ChangeStatusInput = input("What would you like to change the delivery status to?: ")      

    #changing the value in the list and assiging to a new dict
    
    order_list[IndexInput]["status"] = ChangeStatusInput

    with open('db/orders.csv', mode='w', newline='') as file:
        

        fieldnames = ['name', 'address', 'phone','courier','status','items']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
     

        #if file is empty, then write header
        if os.stat("db/orders.csv").st_size == 0:
           writer.writeheader()
           writer.writerows(order_list)
        else:
            writer.writerows(order_list)
    
###################################################################################    
    
def UpdateFullOrder():
    order_list= funcs.readCSVFile('db/orders.csv')
           
    #order_list=[]

    IndexInput = int(input("Which order (index) would you like to update: "))
    nameUpdate = str(input("New name to update or leave blank: "))
    addressUpdate = str(input("New address to update or leave blank: "))
    phoneUpdate = str(input("New phone number to update or leave blank: "))
    courierUpdateString = input("New courier to update or leave blank: ")
    
    itemsUpdateString = input("Please enter items seperated by comma: ")
        

    if nameUpdate== "":
        pass     
    else:
        order_list[IndexInput]["name"] = nameUpdate
        changes_to_order_made = True

    if addressUpdate =="":
        pass
    else:
        order_list[IndexInput]["address"] = addressUpdate
        changes_to_order_made = True

    if phoneUpdate =="":
        pass
    else:
        order_list[IndexInput]["phone"] = phoneUpdate
        changes_to_order_made = True

    if courierUpdateString =="":
        pass
    else:
        order_list[IndexInput]["courier"] = int(courierUpdateString)
        changes_to_order_made = True
    
    if not itemsUpdateString =="":
        itemsUpdate = itemsUpdateString.split(",")
        userNewItems = list(map(int, itemsUpdate))
        order_list[IndexInput]["items"] = userNewItems
        changes_to_order_made = True

    print("\nYour order has been updated")
                           
    with open('db/orders.csv', mode='w', newline='') as file:
        

        fieldnames = ['name', 'address', 'phone','courier','status','items']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        

        #if file is empty, then write header
        if os.stat("db/orders.csv").st_size == 0:
            writer.writeheader()
            writer.writerows(order_list)
        else:
            writer.writerows(order_list)



################################################################################


def DeleteOrder():
    order_list= funcs.readCSVFile('db/orders.csv')
    
    #update
    IndexInput = int(input("Which order (index) would you like to delete: "))
    order_list.pop(IndexInput)
    
    print("\nYour order has been deleted")
    print(order_list)

    #write
    with open('db/orders.csv', 'w', newline= '') as file:
        fieldnames = ['name', 'address', 'phone','courier','status','items']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(order_list)
