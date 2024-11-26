import mysql.connector
from mysql.connector import Error
from sql_connection import Database

class Books:
    def __init__(self, title, author_id, isbn, publication_date, availability):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = True

    def add_book_to_library(self, title, author_id, isbn, publication_date, availability):
        
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        new_book = (title, author_id, isbn, publication_date, availability)
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Inserts a new book into the Books Table
            query = "INSERT INTO Books(title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, new_book)
            database.conn.commit()
            cursor.close()
            print(f"{title} was successfully added to the database.")
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")

    def borrow_book(self, book_id, user_id, borrow_date, return_date):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        is_book_available = (book_id, )
        
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Checks to see if book is available to borrow
            is_available_query = "SELECT availability FROM Books WHERE id = %s"
            cursor.execute(is_available_query, is_book_available)
            available = cursor.fetchall()
            if available:
                # Inserting borrowing information in Borrowed_books Table and updates 'availability' in Books Table
                borrow_query = "INSERT INTO Borrowed_books(book_id, user_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(borrow_query, (book_id, user_id, borrow_date, return_date))
                update_book_query = "UPDATE Books SET availability = FALSE WHERE id = %s"
                cursor.execute(update_book_query, (book_id, ))
                database.conn.commit()
                print("Book has been borrowed successfully!")
            else:
                print("Book is not available to borrow at this time.")
            database.close_connection()
        except Error as e:
            print(f"Error executing query: {e}")

    def return_book(self, book_id):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        book_to_return = (book_id, )
        
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Updates 'availability' in Books Table to show that book is available again
            return_query = "UPDATE Books Set availability = True WHERE id = %s"
            cursor.execute(return_query, book_to_return)
            # Deletes book entry from Borrowed_books Table
            delete_query = "DELETE FROM Borrowed_books WHERE book_id = %s"
            cursor.execute(delete_query, (book_id, ))
            database.conn.commit()
            print("Book has been successfully returned")
            database.close_connection()
        except Error as e:
            print(f"Error executing query: {e}")

    def search_for_a_book(self, title):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        book_to_search = (title, )
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Searches Book Table for a particular book and returns details
            query = "SELECT * FROM Books WHERE title = %s"
            cursor.execute(query, book_to_search)
            book_details = cursor.fetchall()
            if not book_details:
                print(f"{book_to_search} not found in the database")
            else:
                # If book is found, query pulls details from Books and Authors Tables
                book_details_query = """SELECT b.id AS BookID, b.title, a.name AS AuthorName, 
                                        b.publication_date, b.isbn
                                        FROM Books b, Authors a
                                        WHERE b.author_id = a.id AND b.title = %s"""
                cursor.execute(book_details_query, book_to_search)
                book_details = cursor.fetchall()
                print(book_details)
                # Queries if book is available and displays to user if they can borrow it
                is_available_query = "SELECT availability FROM Books WHERE title = %s"
                cursor.execute(is_available_query, book_to_search)
                available = cursor.fetchall()
                if available:
                    print(f"{book_to_search} is available to borrow")
                else:
                    print(f"{book_to_search} is not available to borrow at this time")
            cursor.close()
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")

    def display_all_books(self):
        database = Database('library_management_system_db', 'root', 'my_password', 'localhost')
        try:
            conn = database.connect_database()
            cursor = database.conn.cursor()
            # Displays all books in the Books Table
            query = "SELECT * FROM Books"
            cursor.execute(query)
            for book in cursor.fetchall():
                print(book)
            cursor.close()
            database.close_connection()
            
        except Error as e:
            print(f"Error executing query: {e}")