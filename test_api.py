#coding=utf-8
import flask
import json
from flask import request


'''
flask: web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
'''
#创建一个服务，把当前这个Python文件当做一个服务
server = flask.Flask(__name__)
@server.route('/login', methods=['get', 'post'])
def login():
    #获取通过url请求传参的数据
    username = request.values.get('name')
    pwd = request.values.get('pwd')
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            resu = {'code': 200, 'message': '登录成功'}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code': -1, 'message': '账号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空'}
        return json.dumps(resu, ensure_ascii=False)

if __name__ == "__main__":
    server.run(debug=True, port=8888, host='127.0.0.1')