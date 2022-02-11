################# General Functions to use #####################

def LandingPageText():
    Text1 = """
        #####################
        #     Main Menu     #
        #####################

        0. Exit Application
        1. Products Menu
        2. Couriers Menu
        3. Orders Menu
        
    """ 
    return Text1

def ProductsText():
    Text1 = """
                    
        =========================
        |     Products Menu     |
        =========================
        
        Welcome! You have 5 choices to choose from:

        1. Display the menu
        2. Create product
        3. Update product
        4. Delete a product
        0: Return to Main Menu
        
    """
    return Text1

def CompanyText():
    Text1 = """
                    
        ********************
        *     Couriers     * 
        ********************
        
        Welcome! You have 5 choices to choose from:

        1. Display the couriers
        2. Create a courier
        3. Update a courier
        4. Delete a a courier
        0: Return to Main Menu
    """
    return Text1   

def OrderText():
    Text1 = """
                    
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
    """
    return Text1   