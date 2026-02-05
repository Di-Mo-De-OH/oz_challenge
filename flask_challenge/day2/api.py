from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import BookSchemas

blp = Blueprint("books","books",url_prefix = "/book",description ="book")

books = []

id = 1

@blp.route("/")
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        return books
    
    @blp.response(201,description="book add")
    @blp.arguments(BookSchemas)
    def post(self,new_book):
        global id
        book = {"book_id":id,**new_book}
        id +=1
        books.append(book)
        return book
    
@blp.route("/<int:book_id>")
class Book(MethodView):
    @blp.response(200)
    def get(self,book_id):
        book = next((book for book in books if book["book_id"]==book_id),None)
        if book is None:
            abort(404,message = "book not found")
        return book
    
    @blp.response(200)
    @blp.arguments(BookSchemas)
    def put(self,update_book,book_id):
        book = next((book for book in books if book["book_id"]==book_id),None)
        if book is None:
            abort(404,message = "not found")
        book.update(update_book)
        return book
    
    @blp.response(204)
    def delete(self,book_id):
        global books
        if not any(book for book in books if book["book_id"]== book_id):
            abort(404,message = "book nor found")
        books = [book for book in books if book["book_id"] != book_id ]
        return ""