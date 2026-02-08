from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint("Users","users",description = "Operations on boards",url_prefix = "/user") # 블루프린트를 정의함

#전체 데이터 조회 및 user post(create)생성
@user_blp.route("/")# 기본 라우트는 블루프린트로 인해 /user
class UserList(MethodView): # CBV(class base view)사용
    # ==전체 데이터를 불러오는 get 핸들러==
    def get(self): 
        users = User.query.all() # db에서 전체 데이터를 가져옴
        
        user_data = [{ 
            "id":user.id,
            "name":user.name,
            "email":user.email,
            
            } for user in users]# 가져온 데이터를 어떤식으로 출력할지 정의
        
        return jsonify(user_data)# josn 형태로 return
    
    # ==유저를 생성하는 post 핸들러==
    def post(self):
        data = request.get_json() #클라이언트로 부터 데이터를 받아옴
        

        new_user = User(name = data["name"],email = data["email"])# 데이터를 생성하기전 User클라스에 컬럼들을 클라에서 받아온 데이터랑 매칭시켜줌
        db.session.add(new_user) # db에 post된 데이터 추가
        db.session.commit()# db에 추가된 데이터 저장
        
        return jsonify({"msg":"success create"}),201 # 성공시 메세지 및 status code 201(create) return

# 단일 객체 조회 및 업데이트 삭제
@user_blp.route("/<int:user_id>")# 라우트 주소는 블루프린트로 인한 /user/user_id(int)
class UserResource(MethodView): # CBV(class base view)사용
    # ==단일 유저를 조회하는 get 핸들러==
    def get(self,user_id):
        user = User.query.get_or_404(user_id) # url로 받은 user_id의 user데이터를 db에서 가져옴
        user_data = {
            "id":user.id,
            "name":user.name,
            "email":user.email,
            
        }# 어떤식으로 출력될지 설정
        

        return jsonify(user_data) # json 형태로 return 

    # == put(update) 핸들러 ==
    def put(self,user_id):
        user = User.query.get_or_404(user_id)  # url로 받은 user_id의 user데이터를 db에서 가져옴
        data = request.get_json() # 클라로 부터 받은 데이터 
        user.name = data["name"] # name 값을 클라에서 받아온 데이터랑 매칭
        user.email = data["email"]# email 값을 클라에서 받아온 데이터랑 매칭 
        db.session.commit() # 위에서 매칭된 데이터 값들을 db에 저장
        
        return jsonify({"msg":"success UPDATE"}),200 

    # ==delete 핸들러 ==
    def delete(self,user_id):
        user = User.query.get_or_404(user_id) #  url로 받은 user_id의 user데이터를 db에서 가져옴
        db.session.delete(user) # 받아온 데이터 db에서 삭제
        db.session.commit()# 삭제된 내용을 db에 저장 
        
        return "",204

