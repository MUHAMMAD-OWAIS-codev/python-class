from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (a list of books)
books = []

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify({'message': 'Book added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
