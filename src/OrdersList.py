import csv
import os

def PrintOrder():
    order_list = []

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


def UpdateStatusOrder():
    orderList=[]
    
    with open('orders.csv',mode='r', newline='') as file:
        for order in file:
            #aadd to dict then add it to the list
            details = dict(order)
            print(details)
    
        for i in range(len(orderList)):
            print (i, end = " ")
            print (orderList[i])    
    
        UserInput = int(input("Which order (number) would you like to update: "))
        ChangeInput = input("What would you like to change the status to?: ")      

    print(orderList)
    
    #orderList[UserInput].update({"status":ChangeInput})
    temp_main_order_list[update_full_order_index].update({'Customer Name': full_name_update})

    #['status'].update(ChangeInput)

    print("")
    #print(orderList)
    
    
    #read file
    #show the list with index
    #PrintOrder()

    #ask for user input
    #userSelection = int(input("Select index: "))
    
    #select relevant list
    #change status according to user
    #write to file





#PrintOrder()
#CreateOrder()
UpdateStatusOrder()

# def UpdateFullOrder()

# def DeleteCourier()