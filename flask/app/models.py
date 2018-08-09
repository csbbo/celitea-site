from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False)#前端限制不能超20个字符
    password_hash = db.Column(db.String(128),nullable=False)
    phone_num = db.Column(db.String(11),nullable=False)
    admin = db.Column(db.Integer,default=0)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(30),nullable=False)
    article = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref='article')

class Apply(db.Model):
    __tablename__ = 'apply'
    name = db.Column(db.String(20), nullable=False)
    stu_num = db.Column(db.String(8), nullable=False)
    phone = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(30),nullable=False)
    introduction = db.Column(db.String(60),nullable=False)
    skill = db.Column(db.Text,nullable=False)
    want_learn = db.Column(db.Text,nullable=False)
    think_celitea = db.Column(db.Text,nullable=False)
    avatar_url = db.Column(db.String(20),nullable=False)

    create_time = db.Column(db.DateTime,primary_key=True,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref='apply')
