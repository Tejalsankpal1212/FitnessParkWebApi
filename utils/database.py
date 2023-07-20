import mysql.connector

class dbconnection():
    """docstring for database."""
    def __init__(self):
        super(dbconnection, self).__init__()
    
    @staticmethod
    def connect():
        conn=None
        try:
            conn=mysql.connector.connect(host="localhost",database="fitnesspark_db",username="root",password="1234")
            print("MySQL Database connection successful")
        except Exception as err:
            print(f"Error: '{err}'")
        
        return conn
