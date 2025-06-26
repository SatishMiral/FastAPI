from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {"title": "book1", "author": "author1", "category": "science"},
    {"title": "book2", "author": "author2", "category": "maths"},
    {"title": "book3", "author": "author3", "category": "history"},
    {"title": "book4", "author": "author4", "category": "history"},
    {"title": "book5", "author": "author2", "category": "science"},
]

@app.get("/hello")
def hello():
    return {"hello world!"}

# Implementing simple GET request
@app.get("/books")
def get_books():
    return books

# Implementing Path Parameter
@app.get("/books/{author}")
def get_book(author):
    books_to_return = []
    for book in books:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

# Implementing Query Parameter
@app.get("/book/{author_name}")
def get_book_by_category(author_name, category):
    books_to_return = []
    for book in books:
        if book.get("author").casefold() == author_name.casefold() and \
          book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Implementing simple POST request
@app.post("/books/add_book")
def add_book(data = Body()):
    books.append(data)
    return {"message": "Book added", "book": data}

# Implementing simple PUT request
@app.put("/books/edit_book")
def edit_book(data = Body()):
    for book in books:
        if book.get("title") == data.get("title"):
            book.update(data)
            return {"message": "Book updated", "book": book}
    return {"message": "Book not found"}

# Implementing simple DELETE request
@app.delete("/books/delete_book/{title}")
def delete_book(title):
    for book in books:
        if book.get("title") == title:
            books.remove(book)
            return {"message": "Book deleted", "book": book}
    return {"message": "Book not found"}

# Implementing simple PATCH request
@app.patch("/books/edit_book/{title}")
def edit_book_patch(title, data = Body()):
    for book in books:
        if book.get("title") == title:
            book.update(data)
            return {"message": "Book updated", "book": book}
    return {"message": "Book not found"}