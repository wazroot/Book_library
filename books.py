from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

# list of books
books = [{"id":1,"Title":"War and Peace"}, {"id":2,"Title":"Moby Dick"}, {"id":3,"Title":"Brave New World"}, {"id":4,"Title":"Crime and Punishment"}, {"id":5,"Title":"The Call of the Wild"}]

# defining the welcome message route
@app.route('/welcome', methods=['GET']) 
def welcome_message():
    return 'Welcome to my page! \n url#1: localhost:9999/books, url#2: localhost:9999/books/(type book id here: 1,2 etc.). \n url#1 will show you all the books from my collection \n url#2 will get you specific book from the collection' 

# defining the route to get all the books from sbove list
@app.route('/books', methods=['GET']) 
def get_books():
    return jsonify({'All book titles' : books})

# defining the route to get specific book with its id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND #if no books found with given id -> message to user and 404 pops


if __name__ == '__main__':
    app.run(port=9999)