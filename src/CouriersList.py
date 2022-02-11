import time
import funcs
import csv
import os

def PrintCompany():
    order_list= funcs.readCSVFile('db/couriers.csv')

#########################################################################

def CreateCompany():
    with open('db/couriers.csv', mode='a+', newline='') as file:
        
        orderList=[]

        fieldnames = ['Courier Name', 'Phone Number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
 
        
        courierName = str(input('Enter courier name: '))
        courierNumber = input('Enter courier number: ')
        
                  
        dictToPass ={'Courier Name': courierName,
                    'Phone Number': courierNumber}      

        #if file is empty, then write header
        if os.stat("db/couriers.csv").st_size == 0:
           writer.writeheader()
           writer.writerow(dictToPass)
        else:
            writer.writerow(dictToPass)

#########################################################################

def UpdateCompany():
    order_list= funcs.readCSVFile('db/couriers.csv')

    IndexInput = int(input("Which order (index) would you like to update: "))
    
    courierName = str(input('Enter courier name or leave blank: '))
    courierNumber = str(input('Enter courier number or leave blank: '))
    

    while True:
        if courierName== "":
            pass     
        else:
            order_list[IndexInput]['Courier Name'] = courierName
            changes_to_order_made = True

        if courierNumber =="":
            pass
        else:
            order_list[IndexInput]['Phone Number'] = courierNumber
            changes_to_order_made = True
        break
           
    with open('db/couriers.csv', mode='w', newline='') as file:
        fieldnames = ['Courier Name', 'Phone Number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')        
        if os.stat("db/products.csv").st_size == 0:
            writer.writeheader()
            writer.writerows(order_list)
        else:
            writer.writerows(order_list)

#########################################################################

def DeleteCompany():
    order_list= funcs.readCSVFile('db/couriers.csv')
    
    #update
    IndexInput = int(input("Which courier (index) would you like to delete: "))
    order_list.pop(IndexInput)
    
    print("\nYour order has been deleted. Here is the updated list: ")
    print(order_list)

    #write
    with open('db/couriers.csv', 'w', newline= '') as file:
        fieldnames = ['Courier Name', 'Phone Number']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        if os.stat("db/couriers.csv").st_size == 0:
            writer.writeheader()
            writer.writerows(order_list)
        else:
            writer.writerows(order_list)

#########################################################################    
