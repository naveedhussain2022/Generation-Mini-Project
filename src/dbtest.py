import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Execute SQL query
cursor.execute('SELECT id, product_name, product_price FROM products')
result = cursor.fetchall()

def printProduct():
    print("")
    print('  Current List:   \n')
    
    for items in result:
        print(f'Index: {str(items[0])} | Product: {items[1].upper()} | Price: £{items[2]}')
    
    print("")


printProduct()