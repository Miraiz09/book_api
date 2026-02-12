from flask import Flask,jsonify,request

app = Flask(__name__)


books =[
    {"id":1, "title":"Jujutsu Kaisen", "author":"Gege Akutami"},
    {"id":2, "title":"Chainsaw Man", "author":"Tatsumi Fujimoto"},
    {"id":3, "title":"One Piece", "author":"Eiichiro Oda"},
]

@app.route("/") 
def Greeting():
    return "<p>Welcome Book API!</p>"
       
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({"books": books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"error": "Book not found"}), 404
    
# Update (PUT) operation
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Delete operation
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = True)


