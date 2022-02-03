from ProductsList import *
from CouriersList import CreateCompany, DeleteCompany, PrintCompany, UpdateCompany

LandingPageText = """
    #####################
    #     Main Menu     #
    #####################

    0. Exit Application
    1. Products Menu
    2. Couriers Menu
    3. Orders Menu
    
"""
productsText = """
                
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
CompanyText = """
                
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

#############################################################################

def CourierMenu():
    print(CompanyText)
    while True:
        try:
            selection = input("Enter your selection please: ")

            if selection == "1":
                PrintCompany()
                
            elif selection == "2":
                CreateCompany()
                
            elif selection == "3":
                UpdateCompany()
                
            elif selection == "4":
                DeleteCompany()
                
            elif selection =="0":
                LandingPage()
            else:
                print("Invalid Choice!")
                LandingPage()
        except ValueError:
            print("Please enter only a number!")
    exit      

#############################################################################

def ProductsMenu():
    print(productsText)
    while True:
        try:
            selection = input("Enter your selection please: ")

            if selection == "1":
                PrintMenu()
                
            elif selection == "2":
                CreateProduct()
                
            elif selection == "3":
                UpdateProduct()
                
            elif selection == "4":
                DeleteProduct()
                
            elif selection =="0":
                LandingPage()
            else:
                print("Invalid Choice!")
                LandingPage()
        except ValueError:
            print("Please enter only a number!")
    exit 

#############################################################################

#Main
def LandingPage():
    while True:
        print(LandingPageText)
        input1 = input("Enter choice: ")
        if input1 == "0":
            print("Exit App")
            quit()
        elif input1 =="1":
            ProductsMenu()

        elif input1 =="2":
            CourierMenu()

        elif input1 =="3":
            False
        else:
            print("Enter a number!")
    exit



###############################
                              
if __name__ == "__main__":    
    LandingPage()             

###############################                     

