import pymysql
from dotenv import load_dotenv
import os



def getConnection():
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
    
    return connection