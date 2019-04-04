# 从flask中导入Flask模块（类）
from flask import Flask, render_template

# 导入SQLAlchemy类
from flask_sqlalchemy import SQLAlchemy

import os

# 实例化一个flask对象
app = Flask(__name__)
# 连接mysql数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "suijizifuchuan"
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/users/")
app.debug = False
db = SQLAlchemy(app)

# 从app中home包中导入实例化的home蓝图对象并重命名
from app.home import home as home_blueprint
# 从app中admin包中导入实例化的admin蓝图对象并重命名
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("/home/404.html"), 404
