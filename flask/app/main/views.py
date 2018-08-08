from flask import render_template,request,redirect,session,g,url_for,current_app
from . import main
from ..models import User,Article,Apply
from .. import db
from datetime import datetime
from flask_login import login_required
import json
from .useJWT import make_jwt,verify_tokent

# 测试
@main.route('/test/',methods=['POST','GET'])
def test():
    allow = request.headers.get('Accept')
    content_encoding = request.headers.get('Accept-Encoding')
    content_length = request.headers.get('Connection')
    user_agent = request.headers.get("User-Agent")
    content_type = request.headers.get('Cookie')
    authorization = request.headers.get('WWW-Authenticate')
    # username = request.form.get('username')
    # password = request.form.get('password')
    username = "chen"
    phone_num = "13978901767"
    print("###################################")
    token = make_jwt(username,phone_num)
    token = token.decode('ascii')
    return json.dumps({'state':'shaobo yes',"token":token})

# 首页
@main.route('/',methods=['GET'])
def index():
    articles = Article.query.all()
    return json.dumps(articles)

# 注册
@main.route('/regist/',methods=['POST'])
def regist():
    username = request.form.get('userName')
    password = request.form.get('userPassword')
    phone_num = request.form.get('userPhoneNumber')
    sms = request.form.get('userIdentifyingCode')
    if sms == '0000':
        user = User.query.filter(User.phone_num == phone_num).first()
        if user:            #手机号已经被使用
            return json.dumps({'registerStatus':'fail'})
        else:
            user = User(username=username,password=password,phone_num=phone_num)
            db.session.add(user)
            db.session.commit()
            return json.dumps({'registerStatus':'success'})
    else:
        return json.dumps({'registerStatus':'wrongCode'})

# 登录
@main.route('/login/',methods=['POST'])
def login():
    phone_num = request.form.get('userPhoneNumber')
    password = request.form.get('userPassword')
    user = User.query.filter(User.phone_num==phone_num).first()
    if user and user.verify_password(password):
        token = make_jwt(user.username,phone_num)
        token = token.decode('ascii')
        return json.dumps({'loginStatus':'true','userName':user.username,"token":token})
    else:
        return json.dumps({'loginStatus':'false'})

# 注销
@main.route('/logout/',methods=['POST'])
def logout():
    out = request.form.get('logout')
    if out == 'true':
        if hasattr(g,'user'):
            session.pop('user_id')
    return json.dumps({'logout':'true'})

# 报名接口
@main.route('/apply_port/',methods=['POST'])
def apply_port():
    token = request.headers.get('Authorization')
    token = token.encode('ascii')
    if verify_tokent(token):
        return json.dump({'loginStatu':'success'})
    else:
        return json.dump({'loginStatu':'fail'})


        

#########################################################
# 作用于每次请求之前
# @main.before_request
# def my_before_request():
#         user_id = session.get('user_id')
#         if user_id:         #本次请求用户存在
#                 user = User.query.filter(User.id==user_id).first()
#                 if user:    #数据库中存在该用户
#                     g.user = user #将该用户置入全局变量g

# # 上下文处理器---在模板中使用
# @main.context_processor
# def my_context_processor():
#         if hasattr(g,'user'):
#                 return {'user':g.user}
#         return {}
