import time
import funcs
import csv
import os

def PrintProduct():
    order_list= funcs.readCSVFile('db/products.csv')

#########################################################################

def CreateProduct():
    with open('db/products.csv', mode='a+', newline='') as file:
        
        orderList=[]

        fieldnames = ['Product Name', 'Product Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
 
        
        productName = str(input('Enter product name: '))
        productPrice = float(input('Enter product price: '))
        
                  
        dictToPass ={'Product Name': productName,
                    'Product Price': productPrice}      

        #if file is empty, then write header
        if os.stat("db/products.csv").st_size == 0:
           writer.writeheader()
           writer.writerow(dictToPass)
        else:
            writer.writerow(dictToPass)

#########################################################################

def UpdateProduct():
    order_list= funcs.readCSVFile('db/products.csv')

    IndexInput = int(input("Which order (index) would you like to update: "))
    
    productUpdate = str(input("New product name to update or leave blank: "))
    productPriceUpdate = float(input("New price to update or leave blank: "))
    

    while True:
        if productUpdate== "":
            pass     
        else:
            order_list[IndexInput]['Product Name'] = productPriceUpdate
            changes_to_order_made = True

        if productPriceUpdate =="":
            pass
        else:
            order_list[IndexInput]['Product Price'] = productPriceUpdate
            changes_to_order_made = True
        break
           
    with open('db/products.csv', mode='w', newline='') as file:
        fieldnames = ['Product Name', 'Product Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')        
        if os.stat("db/products.csv").st_size == 0:
            writer.writeheader()
            writer.writerows(order_list)
        else:
            writer.writerows(order_list)



#########################################################################

def DeleteProduct():
    order_list= funcs.readCSVFile('db/products.csv')
    
    #update
    IndexInput = int(input("Which order (index) would you like to delete: "))
    order_list.pop(IndexInput)
    
    print("\nYour order has been deleted")
    print(order_list)

    #write
    with open('db/products.csv', 'w', newline= '') as file:
        fieldnames = ['Product Name', 'Product Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(order_list)