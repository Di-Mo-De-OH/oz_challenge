from flask import Flask
from flask_smorest import Api
from flask import render_template

from db import db
from models import User,Board
from routes.board import board_blp
from routes.user import user_blp


app = Flask(__name__)  # flask 인스턴스 생성

# db설정
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:oz-password@localhost/oz"  # sqlalchemy가 사용할 db 연결

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #모델 변경 사항 추적 기능 비활성화


db.init_app(app) #flask 앱과 sqlalchemy 연결

#api 문서 설정
app.config["API_TITLE"] = "My API" 
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)# flask_smorest api 객체 생성

api.register_blueprint(board_blp) # board를 블루 프린트 라우팅
api.register_blueprint(user_blp) # user를 블루 프린트 라우팅


# 클라이언트 라우팅
@app.route("/manage-boards") # 실제 유저에게 보여주는 클라이언트 라우팅 서버주소는 /manage-boards
def manage_boards(): 
    return render_template("boards.html") # templates속 boards.html을 라우팅 시켜줌

@app.route("/manage-users")# 실제 유저에게 보여주는 클라이언트 라우팅 서버주소는 /manage-users
def manage_users():
    return render_template("users.html")# templates속 users.html을 라우팅 시켜줌


if __name__ =="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
