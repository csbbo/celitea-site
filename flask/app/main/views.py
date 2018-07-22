from flask import render_template,request,redirect,session,g,url_for
from . import main
from ..models import User,Article,Apply
from .. import db
from datetime import datetime
from flask_login import login_required
import json

# 测试
@main.route('/test',methods=['POST','GET'])
def test():
    d = {'name': 'xmr', 'age': 18}
    return json.dumps(d)

# 注册
@main.route('/regist',methods=['POST'])
def regist():
    username = request.form.get('username')
    password = request.form.get('password')
    phone_num = request.form.get('phone_num')
    print('############################################################')
    print(username)
    print(password)
    print(phone_num)
    user = User.query.filter(User.phone_num == phone_num).first()
    if user:            #手机号已经被使用
        return json.dumps({'state':'fail'})
    else:
        user = User(username=username,password=password,phone_num=phone_num)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        session.permanent = True
        return json.dumps({'state':'ok'})
        # return "successs!"

# 登录
@main.route('/login/',methods=['POST'])
def login():
    phone_num = request.form.get('phone_num')
    password = request.form.get('password')
    user = User.query.filter(User.phone==phone).first()
    if user and user.verify_password(password):
        session['user_id'] = user.id
        session.permanent = True
        return json.dumps({'state':'ok'})
    else:
        return json.dumps({'state':'fail'})

# 注销
@main.route('/logout/',methods=['POST'])
def logout():
    if hasattr(g,'user'):
        session.pop('user_id')
    return json.dumps({'state':'ok'})


#########################################################
# 每次请求之前
@main.before_request
def my_before_request():
        user_id = session.get('user_id')
        if user_id:         #本次请求用户存在
                user = User.query.filter(User.id==user_id).first()
                if user:    #数据库中存在该用户
                    g.user = user #将该用户置入全局变量g

# 上下文处理器---在模板中使用
@main.context_processor
def my_context_processor():
        if hasattr(g,'user'):
                return {'user':g.user}
        return {}
