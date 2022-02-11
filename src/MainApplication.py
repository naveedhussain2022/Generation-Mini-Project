from ProductList import PrintProduct, CreateProduct, UpdateProduct, DeleteProduct
from CouriersList import CreateCompany, DeleteCompany, PrintCompany, UpdateCompany
from OrdersList import PrintOrder,CreateOrder,UpdateStatusOrder,UpdateFullOrder,DeleteOrder
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
                PrintCompany()
                
            elif selection == "2":
                CreateCompany()
                
            elif selection == "3":
                UpdateCompany()
                
            elif selection == "4":
                DeleteCompany()
                
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
                PrintProduct()
                time.sleep(2)
                
            elif selection == "2":
                CreateProduct()
                
            elif selection == "3":
                UpdateProduct()
                
            elif selection == "4":
                DeleteProduct()
                
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
                PrintOrder()
                
            elif selection == "2":
                CreateOrder()
                
            elif selection == "3":
                UpdateStatusOrder()
                
            elif selection == "4":
                UpdateFullOrder()
            
            elif selection =="5":
                DeleteOrder() 

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

###############################
                              
Main()             

###############################                     

