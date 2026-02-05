from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import BookSchemas

blp = Blueprint("books","books",url_prefix = "/book",description ="book")

books = []



@blp.route("/")
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        return books
    
    @blp.response(201,description="book add")
    @blp.arguments(BookSchemas)
    def post(self,new_book):
        books.append(new_book)
        return new_book
    
@blp.route("/<string:title>")
class Book(MethodView):
    @blp.response(200)
    def get(self,title):
        book = next((book for book in books if book["title"]==title),None)
        if book is None:
            return abort(404,message = "book not found")
        return book
    
    @blp.response(200)
    @blp.arguments(BookSchemas)
    def put(self,update_book,title):
        book = next((book for book in books if book["title"]==title),None)
        if book is None:
            return abort(404,message = "not found")
        book.update(update_book)
        return update_book
    
    @blp.response(204)
    def delete(self,title):
        global books
        if not any(book for book in books if book["title"]== title):
            abort(404,message = "book nor found")
        books = [book for book in books if book["title"] != title ]
        return ""