from ast import Pass
import pymysql
import os
import time
import db
from locale import currency
from unittest import result
from dotenv import load_dotenv

# Remember to close liveshare!!!

connection = db.getConnection()
cursor = connection.cursor()


###########################################################################################

def printOrder():
    result = cursor.execute('SELECT orders.id, customer_name, customer_address, customer_phone, courier, order_status, \
                            group_concat(products.product_name) from orders \
                            join products_on_orders on orders.id = products_on_orders.order_id \
                            join products on products_on_orders.product_id = products.id where orders.id \
                            group by orders.id')
    result = cursor.fetchall()
    
    print("")
    print('  Current List:   \n')
    for items in result:
        print(f'ID: {str(items[0])} | Name: {items[1].upper()} | Address: {str(items[2])} | Phone: {str(items[3])} | Courier: {(items[4])} | Status: {str(items[5])} | Product: {str(items[6])}')
    print("")

############################################################################################

def createOrder():
    
    orderName = input('Enter order name: ')
    orderAddress = input('Enter order address: ')
    orderPhone = input('Enter order phone number: ')
    
    #Courier
    print("")
    courierDisplay = "SELECT id, courier_name from couriers"
    result = cursor.execute(courierDisplay)
    result = cursor.fetchall()
    for order in result:
        print(f'ID: {str(order[0])} | Courier: {order[1]}')
    print("")
    orderCourier = int(input('Enter (ID) for courier: '))
    print("")

    #Status
    orderList = ["Preparing", "Out for delivery", "Delivered"]
    for i, item in enumerate(orderList):
        print(f'Index:{i} | {item}')
    print("")
    orderStatus = int(input('Enter order status: '))
    newOrderStatus = orderList[orderStatus]
    
    sql = "INSERT INTO orders (customer_name, customer_address,customer_phone,courier,order_status) VALUES (%s, %s,%s,%s,%s)"
    val = (orderName,orderAddress,orderPhone,orderCourier,newOrderStatus)
    cursor.execute(sql,val)
    connection.commit()

    getOrderId = cursor.lastrowid
    print("")

    #Products
    displayProducts = cursor.execute("select id, product_name from products")
    displayProducts = cursor.fetchall()
    for items in displayProducts:
        print(f'Index: {str(items[0])} | Name: {items[1]}')

    products = []
    orderProducts = input('\nEnter products seperated by comma (1,1,3,6): ')
    newProducts = orderProducts.split(",")

    for i in newProducts:
        products.append((getOrderId,i)) 

    sql = "INSERT INTO products_on_orders (order_id,product_id) VALUES (%s,%s)"
    cursor.executemany(sql,products)
    connection.commit()

    

    print("")
    print("Your order has been added. Here is the new orders list: \n")
    time.sleep(2)
    printOrder()

############################################################################################

def updateOrderStatus():
    printOrder()
    
    idInput = int(input("Which order (ID) would you like to update: "))


    orderList = ["Preparing", "Out for delivery", "Delivered"]
    for i, item in enumerate(orderList):
        print(f'Index:{i} | {item}')
    orderStatus = int(input('Enter order status: '))
    newOrderStatus = orderList[orderStatus]
    
    sql = "UPDATE orders SET order_status=%s  WHERE id= %s"
    val = (newOrderStatus,idInput)
    cursor.execute(sql,val)
    connection.commit()

    print("")
    print("Your status has been added. Here is the new orders list: \n")
    time.sleep(2)
    printOrder()


############################################################################################

def updateOrder():
    
    printOrder()
    
    idInput = int(input("Which order (ID) would you like to update: "))
    nameOrderUpdate = str(input("New order name to update or leave blank: "))
    addressOrderUpdate = input("New address to update or leave blank: ")
    phoneOrderUpdate = input("New phone to update or leave blank: ")
    print("")
    
    #Courier Update
    courierDisplay = "SELECT id, courier_name from couriers"
    result = cursor.execute(courierDisplay)
    result = cursor.fetchall()
    for order in result:
        print(f'Index: {str(order[0])} | Courier: {order[1]}')
    print("")
    orderCourier = input('Enter (ID) for courier: ')
    print("")

    #Update product
    displayProducts = cursor.execute("select id, product_name from products")
    displayProducts = cursor.fetchall()
    
    products =[]
    for items in displayProducts:
        print(f'Index: {str(items[0])} | Name: {items[1]}')
    
    orderProducts = input('\nEnter products seperated by comma (1,1,3,6): ')
    newProducts = orderProducts.split(",")


    #Update the database
    if nameOrderUpdate== "":
        pass
    else:
        sql = 'UPDATE orders set customer_name = %s  WHERE id = %s'
        val = (nameOrderUpdate, idInput)
        cursor.execute(sql, val)
        connection.commit()
    
    if addressOrderUpdate =="":
        pass
    else:
        sql = 'UPDATE orders set customer_address = %s  WHERE id = %s'
        val = (addressOrderUpdate, idInput)
        cursor.execute(sql, val)
        connection.commit()

    if phoneOrderUpdate =="":
        pass
    else:
        sql = 'UPDATE orders set customer_phone = %s  WHERE id = %s'
        val = (phoneOrderUpdate, idInput)
        cursor.execute(sql, val)
        connection.commit()

    if orderCourier =="":
        pass
    else:
        sql = 'UPDATE orders set courier = %s  WHERE id = %s'
        val = (int(orderCourier), idInput)
        cursor.execute(sql, val)
        connection.commit()
    
    if newProducts =="":
        pass
    else:
        sql = "DELETE FROM products_on_orders  WHERE order_id = %s"
        cursor.execute(sql,idInput)

        for i in newProducts:
            products.append((idInput,i)) 

        sql = "INSERT INTO products_on_orders (order_id,product_id) VALUES (%s,%s)"
        cursor.executemany(sql,products)
        connection.commit()

    print("")
    print("Your order has been added. Here is the new orders list: \n")
    time.sleep(2)
    printOrder()

# ###########################################################################################


def deleteOrder():
    printOrder()
    
    idInput = int(input("Which order (ID) would you like to delete: "))

    sql = 'DELETE FROM orders WHERE id = %s'
    val = (idInput)
    
    cursor.execute(sql,val)
    connection.commit()    

    print("Order has been deleted. Here is the new order list:")
    time.sleep(2)
    printOrder()



