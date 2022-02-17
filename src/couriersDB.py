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


def printCourier():
    result = cursor.execute('SELECT id, courier_name, courier_phone FROM couriers')
    result = cursor.fetchall()
    
    print("")
    print('  Current List:   \n')
    for items in result:
        print(f'Index: {str(items[0])} | Courier: {items[1].upper()} | Phone Number: {str(items[2])}')
    print("")

###########################################################################################


def createCourier():
    
    courierName = str(input('Enter courier name: '))
    courierPrice = int(input('Enter courier phone number: '))
    
    
    sql = "INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)"
    val = (courierName,courierPrice)
    
    cursor.execute(sql,val)
    connection.commit()
    
    print("")
    print("Your couriers has been added. Here is the new couriers list: \n")
    time.sleep(2)
    
    printCourier()

###########################################################################################

def updateCourier():
    
    printCourier()
    
    idInput = int(input("Which order (index) would you like to update: "))
    courierNameUpdate = str(input("New courier name to update or leave blank: "))
    courierNumberUpdate = input("New courier number to update or leave blank: ")
    
    
    if courierNameUpdate== "":
        pass
    else:
        sql = 'UPDATE couriers set courier_name = %s  WHERE id = %s'
        val = courierNameUpdate, idInput
        
        cursor.execute(sql, val)
        connection.commit()
    
    if courierNameUpdate =="":
        pass
    else:
        sql = 'UPDATE couriers set courier_phone = %s  WHERE id = %s'
        val = int(courierNumberUpdate), idInput
        
        cursor.execute(sql, val)
        connection.commit()

    printCourier()

###########################################################################################


def deleteCourier():
    printCourier()
    
    idInput = int(input("Which order (index) would you like to delete: "))

    sql = 'DELETE FROM couriers WHERE id = %s'
    val = (idInput)
    
    cursor.execute(sql,val)
    connection.commit()    

    print("Courier has been deleted. Here is the couriers")
    time.sleep(2)
    printCourier()

###########################################################################################
