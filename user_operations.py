import mysql.connector
from mysql.connector import Error
from sql_connection import Database

class LibraryUser:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_user(self, name, library_id):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        new_user = (name, library_id)
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Inserting a new user into the database
            query = "INSERT INTO Users(name, library_id) VALUES (%s, %s)"
            cursor.execute(query, new_user)
            database.conn.commit()
            cursor.close()
            print(f"{name} was successfully added to the database.")
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")
    
    def search_for_a_user(self, name):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        user_to_search = (name, )
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Searches database to see if there is an entry for this user
            query = "SELECT * FROM Users WHERE name = %s"
            cursor.execute(query, user_to_search)
            user_details = cursor.fetchall()
            if not user_details:
                print(f"{user_to_search} not found in database")
            else: 
                # Queries the Books, Users, and Borrowed_books Tables to get user details
                user_details_query = """SELECT u.id AS UserID, u.name AS Username, u.library_id, b.title
                                        FROM Users u, Borrowed_books bb, Books b
                                        WHERE u.id = bb.user_id AND bb.book_id = b.id;"""
                cursor.execute(user_details_query)
                user_details = cursor.fetchall()
                print(user_details)
            cursor.close()
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")

    def display_all_users(self):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Displays all users
            query = "SELECT * FROM Users"
            cursor.execute(query)
            for user in cursor.fetchall():
                print(user)
            cursor.close()

            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")