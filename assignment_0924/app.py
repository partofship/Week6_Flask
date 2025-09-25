from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import User, Board
from urllib.parse import quote_plus


app = Flask(__name__)
pw = quote_plus("l3yl3yp0rt@$")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{pw}@localhost/study01'
# 디버깅 1) pw에 @가 들어가 있어서 인식 오류, fstring으로 해결 2) schema 없음으로 인해 접속 안 되던것, MySQL에서 스키마 생성으로 해결.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #True로 하면 리소스 많이 잡아먹어요
db.init_app(app)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

from routes.users import user_blp
from routes.board import board_blp

api = Api(app)
api.register_blueprint(user_blp)
api.register_blueprint(board_blp)

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        print("여기 실행?")
        db.create_all()
    app.run(debug=True)