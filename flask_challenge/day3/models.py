from db import db

# user db 생성을 위한 클라스
class User(db.Model): 
    __tablename__ = "users" # 테이블 이름 설정
    # 아래는 각각의 컬럼에 어떤 속성을 넣을지 모델링
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(100),unique = True,nullable=False)
    boards = db.relationship("Board",back_populates = "author",lazy = "dynamic")

# board db 생성을 위한 클라스
class Board(db.Model):
    __tablename__ = "boards"  # 테이블 이름 설정
    # 아래는 각각의 컬럼에 어떤 속성을 넣을지 모델링
    id = db.Column(db.Integer,primary_key = True,)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable = False)
    author = db.relationship("User",back_populates="boards")

