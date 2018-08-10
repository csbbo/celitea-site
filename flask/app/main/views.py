from flask import render_template,request,redirect,session,g,url_for,current_app,jsonify
from . import main
from ..models import User,Article,Apply
from .. import db
from datetime import datetime
from flask_login import login_required
import json
from .useJWT import make_jwt,verify_tokent
from .sms import requestSmsCode,verifySmsCode
from sqlalchemy.ext.declarative import DeclarativeMeta


# 测试
@main.route('/test/',methods=['POST','GET'])
def test():
    allow = request.headers.get('Accept')
    content_encoding = request.headers.get('Accept-Encoding')
    content_length = request.headers.get('Connection')
    user_agent = request.headers.get("User-Agent")
    content_type = request.headers.get('Cookie')
    authorization = request.headers.get('WWW-Authenticate')
    username = "chen"
    phone_num = "13978901767"
    token = make_jwt(username,phone_num)
    token = token.decode('ascii')
    name = "陈少波"
    return jsonify({'state':'shaobo yes','name':name})

# 首页
@main.route('/',methods=['GET'])
def index():
    # resp.headers['Content-Encoding'] = 'utf-8'
    temp = []
    articles = Article.query.all()
    for tmp in articles:
        temp.append(tmp.to_json())
    resp = jsonify(temp)
    return resp

# 注册
@main.route('/regist/',methods=['POST'])
def regist():
    username = request.form.get('userName')
    password = request.form.get('userPassword')
    phone_num = request.form.get('userPhoneNumber')
    sms = request.form.get('userIdentifyingCode')
    # if verifySmsCode(phone_num,sms) == 'ok':
    if sms == '0000':
        user = User.query.filter(User.phone_num == phone_num).first()
        if user:            #手机号已经被使用
            return jsonify({'registerStatus':'fail'})
        else:
            user = User(username=username,password=password,phone_num=phone_num)
            db.session.add(user)
            db.session.commit()
            return jsonify({'registerStatus':'success'})
    else:
        return jsonify({'registerStatus':'wrongCode'})

# 登录
@main.route('/login/',methods=['POST'])
def login():
    phone_num = request.form.get('userPhoneNumber')
    password = request.form.get('userPassword')
    user = User.query.filter(User.phone_num==phone_num).first()
    if user and user.verify_password(password):
        token = make_jwt(user.username,phone_num)
        token = token.decode('ascii')
        return jsonify({'loginStatus':'true','userName':user.username,"token":token})
    else:
        return jsonify({'loginStatus':'false'})



# 申请验证码
@main.route('/sms/',methods=['POST'])
def sms():
    phone = request.form.get('phone')
    send = {
        'smsId':requestSmsCode(phone)
    }
    return jsonify(send)

# 注销
@main.route('/logout/',methods=['POST'])
def logout():
    out = request.form.get('logout')
    if out == 'true':
        if hasattr(g,'user'):
            session.pop('user_id')
    return jsonify({'logout':'true'})

# # 报名接口
# @main.route('/apply/',methods=['POST'])
# def apply_port():
#     token = request.headers.get('Authorization')
#     token = token.encode('ascii')
#     if verify_tokent(token):
#         return json.dump({'loginStatu':'success'})
#     else:
#         return json.dump({'loginStatu':'fail'})

# 报名表
@main.route('/applications/',methods=['POST'])
def applications():
    name = request.form.get('name')
    stu_num = request.form.get('stu_num')
    phone = request.form.get('phone')
    email = request.form.get('email')
    introduction = request.form.get('introduction')
    skill = request.form.get('skill')
    want_learn = request.form.get('want_learn')
    think_celitea = request.form.get('think_celitea')
    avatar_url = request.form.get('avatar')
    token = request.headers.get('Authorization')
    token = token.encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        apply = Apply(name=name,stu_num=stu_num,phone=phone,email=email,introduction=introduction, \
                skill=skill,want_learn=want_learn,think_celitea=think_celitea,avatar_url=avatar_url,user_id=user.id)
        db.session.add(apply)
        db.session.commit()
        return jsonify({'apply':'success'})
    else:
        return jsonify({'loginStatu':'fail'})

# 报名列表
@main.route('/applylist/',methods=['GET'])
def applylist():
    token = request.headers.get('Authorization')
    token = token.encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.admin == 1:
            temp = []
            alist = Apply.query.all()
            for tmp in alist:
                temp.append(tmp.to_json())
            resp = jsonify(temp) 
            return resp
        else:
            return jsonify({'isadmin':'no'})
    else:
        return jsonify({'loginStatu':'fail'})


# 管理页面
# @main.route('/admin/',methods=['GET'])
# def is_admin():
#     pass
        
# 添加文章
@main.route('/articles/',methods=['POST'])
def articles():
    article_title = "title"
    article = request.form.get('article')
    token = request.headers.get('Authorization')
    token = token.encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.admin == 1:
            article = Article(article_title=article_title,article=article,user_id=user.id,\
                        create_time=datetime.now())
            db.session.add(article)
            db.session.commit()
            return jsonify({'add_article':'success'})
        else:
            return jsonify({'add_article':'fail'})
    else:
        return jsonify({'loginStatu':'fail'})

# 修改文章
@main.route('/mod_articles/',methods=['POST'])
def mod_articles():
    pass


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
