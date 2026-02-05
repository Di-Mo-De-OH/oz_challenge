from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import BookSchemas

blp = Blueprint("books","books",url_prefix = "/book",description ="book")

books = [] # db 대신에 임시용으로 사용할 리스트

id = 1 # id 값을 자동적으로 주기 위한 값

@blp.route("/") # 기본 라우트를 /로 설정 하지만 위에 blp의 url_prefix를 받아와서 /book/ 로 라우팅 됌
class BookList(MethodView): # book_id를 필요로 하지 않는 핸들러에 대한 클래스
    @blp.response(200) # 성공시 200 으로 맵핑해줌
    def get(self): # 모든 book 정보에 대한 get핸들러
        return books # 성공시 books 리스트 반환
    
    @blp.response(201,description="book add") 
    @blp.arguments(BookSchemas) # BookSchemas 에 정의된 데이터로 유효성 검사  및 값을 뱉어줌
    def post(self,new_book): # create 를 위한 post 핸들러 및 위에서 뱉어준 값을 new_book에 담음
        global id # id 값을 주기 위해 클라스 외부에 정의된 변수 id 가져오기
        book = {"book_id":id,**new_book} # 어떤 형식으로 list를 만들지 정의
        id +=1 # 정의후 id 값이 겹치면 안돼기 떄문에 +1을 실행
        books.append(book) # 데이터 append
        return book # 어떤 데이터가 post 되었는지 반환
    
@blp.route("/<int:book_id>") # id 를 필요로 하는 핸들러들을 위한 클라스
class Book(MethodView): 
    @blp.response(200) 
    def get(self,book_id): # 개별 book 에 대한 get 핸들러
        book = next((book for book in books if book["book_id"]==book_id),None) # id 값이 실재로 존재하는지 확인 및 그 값을 가져옴
        if book is None: # book 값이 유효한지 아닌지 판단하는 조건문
            abort(404,message = "book not found") # 없다면 에러 발생
        return book # 있다면 출력
    
    @blp.response(200)
    @blp.arguments(BookSchemas) # 여기서 BookSchemas 검증이 정상적으로 돼면 값을 반환시켜줌 
    def put(self,update_book,book_id): # 업데이트를 위한  put 핸들러 및 위에서 반환된 값을 update_book으로 받음  
        book = next((book for book in books if book["book_id"]==book_id),None) 
        if book is None:
            abort(404,message = "not found")
        book.update(update_book) # 있다면 book 데이터를 업데이트 시켜줌 
        return book # book 반환
    
    @blp.response(204)
    def delete(self,book_id):# delete 핸들러
        global books # books 리스트를 재정의 하기 위해 class 외부에 정의된 books 를 받아옴
        if not any(book for book in books if book["book_id"]== book_id): # id 가 유효한지 확인
            abort(404,message = "book nor found")# 없다면 오류
        books = [book for book in books if book["book_id"] != book_id ] # 있다면 url 로 받은 book_id 값을 뺴고 books 리스트를 재정의 하므로써 delete 시킴
        return ""