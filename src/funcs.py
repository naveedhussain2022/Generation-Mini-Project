import csv

def readCSVFile(filename):
    order_list = []
    with open(filename, 'r', newline= '') as file:
        items_in_list = csv.DictReader(file)
        print("")
        print('  Current List:   \n')    
        i = 0
        for row in items_in_list:
            print("Index : "+ str(i),row)
            i += 1
            order_list.append(row)
        print('\n')
    return order_list


    