import couriersDB
import productsDB
import ordersDB
import time

def CourierMenu():
    #print(CompanyText())
    while True:
        
            selection = input("""
                    
        ********************
        *     Couriers     * 
        ********************
        
        Welcome! You have 5 choices to choose from:

        1. Display the couriers
        2. Create a courier
        3. Update a courier
        4. Delete a a courier
        0: Return to Main Menu
        
        \nEnter Selection: """)

            if selection == "1":
                couriersDB.printCourier()
                
            elif selection == "2":
                couriersDB.createCourier()
                
            elif selection == "3":
                couriersDB.updateCourier()
                
            elif selection == "4":
                couriersDB.deleteCourier()
                
            elif selection =="0":
                Main()
            else:
                print("Invalid Choice!")
                Main()

    exit      

#############################################################################

def ProductsMenu():
    #print(ProductsText())
    while True:
        try:
            selection = input("""
                    
        =========================
        |     Products Menu     |
        =========================
        
        Welcome! You have 5 choices to choose from:

        1. Display the menu
        2. Create product
        3. Update product
        4. Delete a product
        0: Return to Main Menu
        
        \nEnter Selection: """)

            if selection == "1":
                productsDB.printProduct()
                time.sleep(2)
                
            elif selection == "2":
                productsDB.createProduct()
                
            elif selection == "3":
                productsDB.updateProduct()
                
            elif selection == "4":
                productsDB.deleteProduct()
                
            elif selection =="0":
                Main()
            else:
                print("Invalid Choice!")
                Main()
        except ValueError as ve:
            print(f'You entered {selection}, which is not a number.')
    exit 

#############################################################################

def OrdersMenu():
    #print(OrderText())
    while True:
        try:
            selection = input("""
                    
        ====================
        =      Orders      = 
        ====================
        
        Welcome! You have 5 choices to choose from:

        1. Display the orders
        2. Create an order
        3. Update the status of an order
        4. Update a complete order
        5: Delete an order
        0: Return to main menu
        
        \nEnter Selection: """)

            if selection == "1":
                ordersDB.printOrder()
                
            elif selection == "2":
                ordersDB.createOrder()
                
            elif selection == "3":
                ordersDB.updateOrderStatus()
                
            elif selection == "4":
                ordersDB.updateOrder()
            
            elif selection =="5":
                ordersDB.deleteOrder() 

            elif selection =="0":
                Main()
            else:
                print("Invalid Choice!")
                Main()
        except ValueError as ve:
            print(f'You entered {selection}, which is not a number.')
    exit 

#############################################################################

def Main():
    while True:
        try:
            input1 = input("""
                #####################
                #     Main Menu     #
                #####################

                0. Exit Application
                1. Products Menu
                2. Couriers Menu
                3. Orders Menu
                
                \nEnter option: """  )

            if input1 == "0":
                print("Exiting App")
                quit()
            elif input1 =="1":
                ProductsMenu()
            elif input1 =="2":
                CourierMenu()
            elif input1 =="3":
                OrdersMenu()
            else:
                print("Enter a number between 0-3!")
        except ValueError as ve:
            print(f'You entered {input1}, which is not a number.')
    exit

###############                              
Main()        #       
###############                     

