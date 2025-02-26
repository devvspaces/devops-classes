# Python Library Management System

## Project Description

Create a simple library management system using Python classes. The system will allow users to add books, check them out, return them, and view the library's collection.

## Learning Objectives

- Creating and using classes
- Implementing class attributes and methods
- Understanding encapsulation
- Working with instance variables
- Class inheritance
- Using special methods like `__str__` and `__repr__`

## Required Classes

1. **Book Class**
   - Attributes: title, author, ISBN, publication_year, genre, availability status
   - Methods: check_out(), return_book(), get_info()

2. **Library Class**
   - Attributes: name, collection (list of Book objects)
   - Methods: add_book(), remove_book(), search_by_title(), search_by_author(), display_all_books()

3. **Member Class**
   - Attributes: name, ID, borrowed_books (list of Book objects)
   - Methods: borrow_book(), return_book(), view_borrowed()

## Extension Ideas

- Create subclasses of Book (like EBook, AudioBook) with additional specific attributes
- Implement data persistence (save/load library state to/from a file)
- Add a simple command-line interface
- Create a Librarian class that inherits from Member but has additional privileges

## Implementation Requirements

- Use proper encapsulation (private/protected attributes where appropriate)
- Include docstrings for classes and methods
- Implement error handling for operations like borrowing unavailable books
- Create at least one class that inherits from another
