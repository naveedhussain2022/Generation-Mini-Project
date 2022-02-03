from MainApplication import *
from MainApplication import LandingPage

def PrintMenu():
    print("")
    file = open('products.txt','r',newline="")
    print(file.read())
    file.close()

#########################################################################

def CreateProduct():
    file = open('products.txt','a',newline="")
    UserInput = input("Enter the product you want to add: ")
    file.write(UserInput +"\n")
    file.close()
    print("")
    PrintMenu()

#########################################################################

def UpdateProduct():
    print("")
    print("### Update Records###")
    print("Here are the products with it's number: ")
    print("")

    ProductList= []

    with open('products.txt','r+') as file:
        for product in file:
            ProductList.append(product.strip())
    
        for i in range(len(ProductList)):
            print (i, end = " ")
            print (ProductList[i])
    
        print("")

        UserInput = int(input("Which product (number) would you like to update: "))
        ChangeInput = input("What would you like to change it to?: ")    
        
        ProductList[UserInput] = ChangeInput

        with open('products.txt', 'w') as file:
            for item in ProductList:
                file.write("%s\n" % item)

    file.close()

    print("")
    print("Here is your new product list")
    
    PrintMenu()

#########################################################################

def DeleteProduct():
    ProductList= []
    with open('products.txt','r+') as file:
        for products in file:
            ProductList.append(products.strip())
    
    for i in range(len(ProductList)):
            print (i, end = " ")
            print (ProductList[i])
    
    print("")

    UserInput = int(input("Which product (number) would you like to delete: "))

    del ProductList[UserInput]

    with open('products.txt', 'w') as file:
        for item in ProductList:
            file.write("%s\n" % item)

    file.close()
    print("")
    print("Products has been deleted")
    PrintMenu()