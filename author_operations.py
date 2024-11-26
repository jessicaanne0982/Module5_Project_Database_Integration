import mysql.connector
from mysql.connector import Error
from sql_connection import Database

class Authors:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_author(self, name, biography):
        
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        new_author = (name, biography)
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Inserting a new author into the Authors Table
            query = "INSERT INTO Authors(name, biography) VALUES (%s, %s)"
            cursor.execute(query, new_author)
            database.conn.commit()
            cursor.close()
            print(f"{name} was successfully added to the database.")
            
        except Error as e:
            print(f"Error executing query: {e}")

    def search_for_an_author(self, name):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        author_to_search = (name, )
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Search for Author name to see if it's in the Authors Table
            query = "SELECT * FROM Authors WHERE name = %s"
            cursor.execute(query, author_to_search)
            author_details = cursor.fetchall()
            if not author_details:
                print(f"{author_to_search} not found in database")
            else:
                print(author_details)
            cursor.close()
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")

    def display_all_authors(self):
            database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
            try:
                conn = database.connect_database()
                cursor = database.conn.cursor()
                # Displays all the authors in the Authors Table
                query = "SELECT * FROM Authors"
                cursor.execute(query)
                for author in cursor.fetchall():
                    print(author)
                cursor.close()

                database.close_connection()
                
            except Error as e:
                print(f"Error executing query: {e}")




