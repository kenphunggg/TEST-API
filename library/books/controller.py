from flask import Blueprint
from .services import (add_book_service, 
                       get_book_by_id_service, 
                       update_book_by_id_service, 
                       delete_book_by_id_service,
                       get_book_by_author_service)

books = Blueprint("books", __name__)
@books.route('/get-all-books')
def get_all_books():
    return "All books"

# Add a new book
@books.route('/book-management/book', methods = ['POST'])
def add_book():
    return add_book_service()

# Get book by ID
@books.route('/book-management/book/<int:id>', methods = ['GET'])
def get_book_by_id(id):
    return get_book_by_id_service(id)

# Update book by ID
@books.route('/book-management/book/<int:id>', methods = ['PUT'])
def update_book_by_id(id):
    return update_book_by_id_service(id)

# Delete book by ID
@books.route('/book-management/book/<int:id>', methods = ['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)

# Get book by author
@books.route('/book-management/book/<string:author>', methods = ['GET'])
def get_book_by_author(author):
    return get_book_by_author_service(author)