import csv

def PrintOrder():
    print("")
    file = open('couriers.txt','r',newline="")
    print(file.read())
    file.close()