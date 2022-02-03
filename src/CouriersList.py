from MainApplication import *

def PrintCompany():
    print("")
    file = open('couriers.txt','r',newline="")
    print(file.read())
    file.close()

#########################################################################

def CreateCompany():
    file = open('couriers.txt','a',newline="")
    UserInput = input("Enter the company you want to add: ")
    file.write(UserInput +"\n")
    file.close()
    PrintCompany()

#########################################################################

def UpdateCompany():
    print("")
    print("### Update Records###")
    print("Here are the couriers with it's number: ")
    print("")

    CourierList= []

    with open('couriers.txt','r+') as file:
        for courier in file:
            CourierList.append(courier.strip())
    
        for i in range(len(CourierList)):
            print (i, end = " ")
            print (CourierList[i])
    
        print("")

        UserInput = int(input("Which courier (number) would you like to update: "))
        ChangeInput = input("What would you like to change it to?: ")    
        
        CourierList[UserInput] = ChangeInput

        with open('couriers.txt', 'w') as file:
            for item in CourierList:
                file.write("%s\n" % item)

    file.close()

    print("")
    print("Here is your new courier list")
    PrintCompany()

#########################################################################

def DeleteCompany():
    
    CourierList= []
    with open('couriers.txt','r+') as file:
        for courier in file:
            CourierList.append(courier.strip())
    
    for i in range(len(CourierList)):
            print (i, end = " ")
            print (CourierList[i])
    
    print("")

    UserInput = int(input("Which courier (number) would you like to delete: "))

    del CourierList[UserInput]

    with open('couriers.txt', 'w') as file:
        for item in CourierList:
            file.write("%s\n" % item)

    file.close()
    print("")
    print("Courier has been deleted")
    PrintCompany()

#########################################################################    

    # CourierList.remove(UserInput)

    # print(CourierList)
    # with open('couriers.txt', 'w') as file:
    #     for item in CourierList:
    #         file.write("%s\n" % item)

    # file.close()

    # print("Here is the menu with it's number: ")
    # for i in range(len(company)):
    #     print (i, end = " ")
    #     print (company[i])

    # UserInput = int(input("Which product (number) would you like to delete: "))
    # del company[UserInput]
    # print(', '.join(company))