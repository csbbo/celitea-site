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
import re


# 首页
@main.route('/',methods=['GET'])
def index():
    # resp.headers['Content-Encoding'] = 'utf-8'
    temp = []
    articles = Article.query.order_by(db.desc(Article.id)).all()
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
        user = User.query.filter_by(phone_num=phone_num).first()
        if user:            #手机号已经被使用
            return jsonify({'registerStatus':'phone_was_us'})
        else:
            user = User(username=username,password=password,phone_num=phone_num,role_id=1)
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
        token = make_jwt(user.phone_num).decode('ascii')
        return jsonify({'userName':user.username,'userRole':user.role.id,'token':token})
    else:
        return jsonify({'login':'fail'})

# 报名
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
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()

        if not Apply.query.filter_by(user_id=user.id).first():
            apply = Apply(name=name,stu_num=stu_num,phone=phone,email=email,introduction=introduction, \
                    skill=skill,want_learn=want_learn,think_celitea=think_celitea,user_id=user.id)
            db.session.add(apply)
            db.session.commit()
            return jsonify({'applications':'success'})
        else:
            return jsonify({'applications':'apply_exist'})
    else:
        return jsonify({'applications':'noLogin'})


# 查看报名列表
@main.route('/apply_list/',methods=['POST'])
def apply_list():
    apply_state = request.form.get('apply_state')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_group_leader():
            temp = []
            if apply_state == 'all_apply':          #所有申请表
                alist = Apply.query.all()
                for tmp in alist:
                    temp.append(tmp.to_json())
                return jsonify(temp)
            elif apply_state == 'notpass_apply':    #未通过的申请表
                alist = Apply.query.filter(Apply.apply_state==1)
                for tmp in alist:
                    temp.append(tmp.to_json())
                return jsonify(temp)
            elif apply_state == 'pass_apply':       #已通过的申请表
                alist = Apply.query.filter(Apply.apply_state==2)
                for tmp in alist:
                    temp.append(tmp.to_json())
                return jsonify(temp)
            # apply_state == 'wait_apply'
            else:                                   #待处理的申请表
                alist = Apply.query.filter(Apply.apply_state==3)
                for tmp in alist:
                    temp.append(tmp.to_json())
                return jsonify(temp)

        else:
            return jsonify({'apply_list':'permissiondeny'})
    else:
        return jsonify({'apply_list':'noLogin'})

# 同意申请
@main.route('/apply_pass/',methods=['POST'])
def apply_pass():
    article_id = request.form.get('apply_id')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_group_leader():
            apply = Apply.query.filter_by(id=article_id).first()
            apply_user = User.query.filter_by(id=apply.user.id).first()
            apply.apply_state = 2
            db.session.add(apply)

            apply_user.role_id = 2    #同时置为成员
            db.session.add(user)
            db.session.commit()

            return jsonify({'apply_pass':'sucess'})
        else:
            return jsonify({'apply_pass':'permissiondeny'})
    else:
        return jsonify({'apply_pass':'noLogin'})

# 拒绝申请
@main.route('/apply_notpass/',methods=['POST'])
def apply_notpass():
    article_id = request.form.get('apply_id')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_group_leader():
            apply = Apply.query.filter_by(id=article_id).first()
            apply_user = User.query.filter_by(id=apply.user.id).first()
            apply.apply_state = 1
            db.session.add(apply)

            apply_user.role_id = 1    #同时置为普通用户
            db.session.add(user)
            db.session.commit()
            return jsonify({'apply_notpass':'success'})
        else:
            return jsonify({'apply_notpass':'permissiondeny'})
    else:
        return jsonify({'apply_notpass':'noLogin'})


# 查看某个报名表内容
@main.route('/apply_detail/',methods=['POST'])
def applylist():
    apply_id = request.form.get("apply_id")
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_group_leader():
            apply_detail = Apply.query.filter(Apply.id==apply_id).first()
            resp = jsonify(apply_detail.to_json())
            return resp
        else:
            return jsonify({'apply_detail':'permissiondeny'})
    else:
        return jsonify({'apply_detail':'noLogin'})


# 添加文章
@main.route('/add_articles/',methods=['POST'])
def articles():
    article = request.form.get('article')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_writer():
            extract_title = re.search(r'<p>(.*)</p>\n([\s\S]*)',article)
            if extract_title:
                article_title = extract_title.group(1)
            else:
                return jsonify({'add_article':'formal_error'})

            article = Article(article_title=article_title,article=article,user_id=user.id,\
                        create_time=datetime.now())
            db.session.add(article)
            db.session.commit()
            return jsonify({'add_article':'success'})
        else:
            return jsonify({'add_article':'permissiondeny'})
    else:
        return jsonify({'add_article':'noLogin'})

# 修改文章
@main.route('/modify_article/',methods=['POST'])
def mod_articles():
    article_content = request.form.get('article')
    article_id = request.form.get('article_id')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        if user.is_writer():
            extract_title = re.search(r'<p>(.*)</p>\n([\s\S]*)',article_content)
            if extract_title:
                article_title = extract_title.group(1)
            else:
                return jsonify({'modify_article':'formal_error'})

            article = Article.query.get(article_id)
            article.article_title = article_title
            article.article = article_content
            db.session.add(article)
            db.session.commit()
            return jsonify({'modify_article':'success'})
        else:
            return jsonify({'modify_article':'permissiondeny'})
    else:
        return jsonify({'modify_article':'noLogin'})

# 获取某一篇文章及其上一篇和下一篇文章
@main.route('/article_detail/',methods=['POST'])
def get_article():
    article_id = request.form.get('article_id')
    article = Article.query.get(article_id)
    try:
        article_previous = Article.query.get(int(article_id)-1).to_json()
    except:
        article_previous  = "None"
    try:
        article_next = Article.query.get(int(article_id)+1).to_json()
    except:
        article_next = "None"
    return jsonify(article.to_json(),article_previous,article_next)

# 获取文章列表
# 可以从首页接口提取

# 添加个人简介
@main.route('/add_bio/',methods=['POST'])
def add_bio():
    bio = request.form.get('bio')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        user.bio = bio
        db.session.add(user)
        db.session.commit()
        return jsonify({'add_bio':'sucess'})
    else:
        return jsonify({'add_bio':'noLogin'})

# 获取个人简介
@main.route('/get_bio/',methods=['GET'])
def get_bio():
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter(User.phone_num==user_phone).first()
        return jsonify({'get_bio':user.bio})
    else:
        return jsonify({'get_bio':'noLogin'})

# 添加和修改用户头像
@main.route('/upload_avatar/',methods=['POST'])
def upload_avatar():
    avatar = request.form.get('avatar')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter_by(phone_num=user_phone).first()
        user.avatar = avatar
        db.session.add(user)
        db.session.commit()
        return jsonify({'upload_avatar':'success'})
    else:
        return jsonify({'upload_avatar':'noLogin'})

# 将用户设置为成员
@main.route('/to_member/',methods=['POST'])
def to_member():
    user_id = request.form.get('user_id')
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter_by(phone_num=user_phone).first()
        if user.is_administrator():
            to_member_user = User.query.filter_by(id=user_id).first()
            to_member_user.role_id = 2
            db.session.add(to_member_user)
            db.session.commit()
            return jsonify({'to_member':'success'})
        else:
            return jsonify({'to_member':'permissiondeny'})
    else:
        return jsonify({'to_member':'noLogin'})

# 申请验证码
@main.route('/sms/',methods=['POST'])
def sms():
    phone = request.form.get('phone')
    send = {
        'smsId':requestSmsCode(phone)
    }
    return jsonify(send)

# 用户列表
@main.route('/user_list/',methods=['GET'])
def user_list():
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter_by(phone_num=user_phone).first()
        if user.is_administrator():
            users = User.query.filter(User.role_id != 5).all()
            temp = []
            for tmp in users:
                temp.append(tmp.to_json())
            return jsonify(temp)
        else:
            return jsonify({'user_list':'permissiondeny'})
    else:
        return jsonify({'user_list':'noLogin'})

# 用户信息
@main.route('/user_detail/',methods=['GET'])
def user_detail():
    token = request.headers.get('Authorization').encode('ascii')
    payload = verify_tokent(token)
    if payload:
        user_phone = payload['phone_num']
        user = User.query.filter_by(phone_num=user_phone).first()
        return jsonify(user.to_json())
    else:
        return jsonify({'user_detail':'noLogin'})
