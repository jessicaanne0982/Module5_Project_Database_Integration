import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self, database, user, password, host):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.connection = None

    def connect_database(self):
        try:
            self.conn = mysql.connector.connect(
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host
            )
            if self.conn.is_connected():
                print("Connection to Library Management System Database was successful")
        except Error as e:
            print(f"Database connection failed. Error: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed")
