from fastapi import FastAPI

app = FastAPI()

books = {
    "book1" : ["name", "author", "genre"],
    "book2" : ["name2", "author2", "genre"]
}

@app.get("/hello")
def hello():
    return {"hello world!"}

@app.get("/books")
def get_books():
    return books