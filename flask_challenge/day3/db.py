from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 
# db.py로 분리하는 이유
# app.py,models.py 간 순환 import 가 발생할 수 있음
# db변수에 담아 전역에서 사용하기 쉽게 하기 위해 
