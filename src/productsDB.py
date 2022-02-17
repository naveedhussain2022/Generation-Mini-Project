import pymysql
import os
import time
import db
from locale import currency
from unittest import result
from dotenv import load_dotenv



connection = db.getConnection()
cursor = connection.cursor()


###########################################################################################


def printProduct():
    result = cursor.execute('SELECT id, product_name, product_price FROM products')
    result = cursor.fetchall()
    
    print("")
    print('  Current List:   \n')
    for items in result:
        amount = items[2]
        price = "{:,.2f}".format(amount)
        print(f'Index: {str(items[0])} | Product: {items[1].upper()} | Price: £{price}')
    print("")

###########################################################################################


def createProduct():
    
    productName = str(input('Enter product name: '))
    productPrice = float(input('Enter product price: '))
    
    
    sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
    val = (productName,productPrice)
    
    cursor.execute(sql,val)
    connection.commit()
    
    print("")
    print("Your product has been added. Here is the new product list: \n")
    time.sleep(2)
    
    printProduct()

###########################################################################################

def updateProduct():
    
    printProduct()
    
    idInput = int(input("Which order (index) would you like to update: "))
    nameProductUpdate = str(input("New product name to update or leave blank: "))
    priceProductUpdate = input("New price to update or leave blank: ")
    
    
    if nameProductUpdate== "":
        pass
    else:
        sql = 'UPDATE products set product_name = %s  WHERE id = %s'
        val = nameProductUpdate, idInput
        
        cursor.execute(sql, val)
        connection.commit()
    
    if priceProductUpdate =="":
        pass
    else:
        sql = 'UPDATE products set product_price = %s  WHERE id = %s'
        val = float(priceProductUpdate), idInput
        
        cursor.execute(sql, val)
        connection.commit()

    printProduct()

###########################################################################################


def deleteProduct():
    printProduct()
    
    idInput = int(input("Which order (index) would you like to delete: "))

    sql = 'DELETE FROM products WHERE id = %s'
    val = (idInput)
    
    cursor.execute(sql,val)
    connection.commit()    

    print("Product has been deleted. Here is the new product")
    time.sleep(2)
    printProduct()

###########################################################################################

#createProduct()
deleteProduct()
#printProduct()