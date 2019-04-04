# 从app包中导入app对象
from app import app
# 可以让flask程序指定端口和ip
from flask_script import Manager

manage = Manager(app)

if __name__ == '__main__':
    manage.run(host='0.0.0.0',port=9988)
