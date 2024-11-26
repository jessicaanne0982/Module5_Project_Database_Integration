from book_operations import Books
from user_operations import LibraryUser
from author_operations import Authors
from sql_connection import Database
from datetime import timedelta
from datetime import date
import re

catalog = Books("title", "author_id", "isbn", "publication_date", "availability")
library_user = LibraryUser("name", "library_id")
author_list = Authors("name", "biography")
database = Database("library_management_system_db", "root", "my_password", "localhost")

def main():
    print("Welcome to the Library Management System!")
    while True:
        main_menu_action = input("\nChoose from the following options: "
                                    "\n1. Book Operations"
                                    "\n2. User Operations"
                                    "\n3. Author Operations"
                                    "\n4. Quit"
                                    "\n")
        if main_menu_action == '4':
            print("Thank you for using the Library Management System! \nExiting now...")
            break
        try:
            if main_menu_action == '1':    
                book_menu_option = input("Book Operations Menu: \nPlease choose from the following options:"
                    "\n1. Add a new book"
                    "\n2. Borrow a book"
                    "\n3. Return a book"
                    "\n4. Search for a book"
                    "\n5. Display all books"
                    "\n")
                try:
                    if book_menu_option == '1':
                        title = input("Enter the name of the book to add: ")
                        author_id = input("Enter the author's ID number: ")
                        isbn = input("Enter the book's ISBN: ")
                        publication_date = input("Enter the publication date: ")
                        book_available = True
                        catalog.add_book_to_library(title, author_id, isbn, publication_date, book_available)
 
                    elif book_menu_option == '2':
                        book_id = input("Enter the book ID to lend: ")
                        user_id = input("Enter the user ID of the person borrowing the book: ") 
                        borrow_date = date.today()
                        return_date = borrow_date + timedelta(days=14)
                        catalog.borrow_book(book_id, user_id, borrow_date, return_date)
                                                   
                    elif book_menu_option == '3':
                        book_id = input("Enter the book ID to return: ")
                        catalog.return_book(book_id)

                    elif book_menu_option == '4': 
                        title = input("Enter the name of the book to search: ")
                        catalog.search_for_a_book(title)

                    elif book_menu_option == '5':
                        catalog.display_all_books()

                except ValueError:
                    print("Invalid option.  Enter a number 1 - 5: ")

            elif main_menu_action == '2':
                user_menu_option = input("User Operations Menu: \nPlease choose from the following options:"
                      "\n1. Add a new user"
                      "\n2. View user details"
                      "\n3. Display all users"
                      "\n")
                try:
                    if user_menu_option == '1':
                        name = input("Enter the user's first and last name: ")
                        library_id = input("Enter the user's 10 digit ID number: ")
                        library_user.add_user(name, library_id)

                    elif user_menu_option == '2':
                        name = input("Enter the user's name to search: ")
                        library_user.search_for_a_user(name)

                    elif user_menu_option == '3':
                        library_user.display_all_users()

                except ValueError:
                    print("Invalid option.  Enter a number 1 - 3: ")

            elif main_menu_action == '3':
                author_menu_option = input("Author Operations Menu: \nPlease choose from the following options:"
                      "\n1. Add a new author"
                      "\n2. View author details"
                      "\n3. Display all authors"
                      "\n")
                try:
                    if author_menu_option == '1':
                        name = input("Enter the author's first and last name: ")
                        biography = input("Enter a short biography of the author: ")
                        author_list.add_author(name, biography)

                    elif author_menu_option == '2':
                        name = input("Enter the author's name to search: ")
                        author_list.search_for_an_author(name)

                    elif author_menu_option == '3':
                        author_list.display_all_authors()

                except ValueError:
                    print("Invalid option.  Enter a number 1 - 3: ")
                    
        except ValueError:
            print("Invalid option.  Enter a number 1 - 4: ")

if __name__ == "__main__":
    main()
            