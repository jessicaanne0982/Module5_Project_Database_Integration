## Library Management System with Database Integration
 
The Library Management System with Databases Integration is an application designed to allow users to easily manage all aspects of the library system - from the catalog of book titles to the list of library users to a directory of authors and their short biographies - all with the power and reliability of a MySQL database in the background.
Created in Python 3.13, this application practices modular program writing and establishing connections between a MySQL database and a Python application.
 
## Installation
 
On a Windows PC, this application can be run in the Command Window.
Mac OS can run within the Terminal Window. Use the package manager pip to install mysql-connector-python, and ensure that the following files are present.

```bash
pip install mysql-connector-python
```
### Necessary files:
#### Main file to execute:
1. Library Management System.py
 
#### Classes within:
1. sql_connection.py 
2. book_operations.py
3. user.py
4. author_operations.py
 
## Usage
 
This a multiple level program that begins by asking the user what type of operation they'd like to perform.
```python
Welcome to the Library Management System!
 
Please Choose from the following menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
```
From here, the user is presented with a number of different menus to perform operations specific to either books, users, or authors. These menus provide a user-friendly way to easily navigate the library management system. All information regarding the books, authors, and users is saved within MySQL tables making accessing specific details simple and efficient.
```python
Book Operations Menu:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
```
```python
User Operations Menu:
1. Add a new user
2. View user details
3. Display all users
```
 
```python
Author Operations Menu:
1. Add a new author
2. View author details
3. Display all authors
```