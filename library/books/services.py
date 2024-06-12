from flask import request, jsonify
import mysql.connector
from library.config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB, DATABASE_PORT


cnx = mysql.connector.connect(user = DATABASE_USER, 
                              password = DATABASE_PASSWORD, 
                              host = DATABASE_HOST, 
                              database = DATABASE_DB, 
                              port= DATABASE_PORT)
cursor = cnx.cursor()

def add_book_service():
    id = request.json['id']
    name = request.json['name']
    page_count = request.json['page_count']
    author_id = request.json['author_id']
    category_id = request.json['category_id']
    action = "INSERT INTO books (id, name, page_count, author_id, category_id) VALUES (%s, %s, %s, %s, %s)"
    values = (id, name, page_count, author_id, category_id)
    try:
        cursor.execute(action, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Add success!"
    except IndentationError:
        return "Can not add book"
    
def get_book_by_id_service(id):
    if id:
        action = "SELECT * FROM books WHERE id = %s"
        value = (id,)
        cursor.execute(action, value)
        book = cursor.fetchone()
        return jsonify(book)
    else:
        return "Not found book"

def update_book_by_id_service(id):
    action_get = "SELECT * FROM books WHERE id = %s"
    value_get = (id,)
    cursor.execute(action_get, value_get)
    book = cursor.fetchone()
    data = request.json
    if book:
        try:
            if data and "page_count" in data:
                action_update = "UPDATE books SET page_count = '%s' WHERE id = '%s'"
                page_count = data["page_count"]
                value_update = (page_count, id)
                cursor.execute(action_update, value_update)
                cnx.commit
                cursor.close
                cnx.close
                return "Book updated!"
            else:
                return "Cannot update book!"
        except IndentationError:
            return "Can not update book!"   
        
def delete_book_by_id_service(id):
    if id:
        try:
            action = "DELETE FROM books WHERE id = %s"
            value = (id,)
            cursor.execute(action, value)
            cnx.commit()
            cursor.close()
            return "Book deleted!"
        except IndentationError:
            return "Can not delete book!"  
    else:
        return "Cannot found book!"

def get_book_by_author_service(author):
    if id:
        action = "SELECT books.id, books.name, books.page_count, books.author_id, books.category_id FROM books CROSS JOIN author WHERE author.name = %s AND books.author_id = author.id "
        value = (author,)
        cursor.execute(action, value)
        book = cursor.fetchone()
        if book:
            return jsonify(book)
        else:
            return "Not found book"

