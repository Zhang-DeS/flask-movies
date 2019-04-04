# 导入蓝图类
from flask import Blueprint

# 实例化一个蓝图对象
home = Blueprint("home", __name__)

# 导入视图包（类）
import app.home.views
