# db_connect.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='saakshi',  # Replace with your password
            database='banking_system'        # Make sure this DB exists
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(" Error connecting to MySQL:", e)
    return None
