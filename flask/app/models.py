from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from datetime import datetime

class Permission:
    IS_VIEWER = 0x01
    MEMBER = 0x02
    WRITE_ARTICLES = 0x04
    GROUP_LEADER = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            '吃瓜群众': (Permission.IS_VIEWER, True),
            '成员': (Permission.IS_VIEWER |
                   Permission.MEMBER , False),
            '组长': (Permission.IS_VIEWER |
                   Permission.MEMBER |
                   Permission.WRITE_ARTICLES, False),
            '文章推送人员': (Permission.IS_VIEWER |
                    Permission.MEMBER |
                    Permission.WRITE_ARTICLES, False),
            '网站管理员': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False)#前端限制不能超20个字符
    password_hash = db.Column(db.String(128),nullable=False)
    phone_num = db.Column(db.String(11),nullable=False)
    avatar = db.Column(db.Text,nullable=True)
    bio = db.Column(db.String(100),nullable=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        dev = "None"
        try:
            for u in self.apply:
                dev = u.apply_state
        except:
            dev = "None"
        return {
            'id':self.id,
            'username':self.username,
            'phone_num':self.phone_num,
            'role_id':self.role_id,
            'apply_state': dev
        }

    def can(self, permissions):
        return self.role is not None and \
               (self.role.permissions & permissions) == permissions

    def is_member(self):
        return self.role.id >= 2

    def is_writer(self):
        return self.role.id >= 3

    def is_group_leader(self):
        return self.role.id >= 4

    def is_administrator(self):
        return self.role.id >= 5

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

    def to_json(self):
        return {
            'id':self.id,
            'article_title':self.article_title,
            'article':self.article,
            'time':self.create_time.strftime('%Y-%m-%d'),
            'user_id':self.user_id
        }

class Apply(db.Model):
    __tablename__ = 'apply'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    stu_num = db.Column(db.String(8), nullable=False)
    phone = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    introduction = db.Column(db.String(60),nullable=False)
    skill = db.Column(db.Text,nullable=False)
    want_learn = db.Column(db.Text,nullable=False)
    think_celitea = db.Column(db.Text,nullable=False)
    apply_state = db.Column(db.Integer,nullable=True,default=3)

    create_time = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref='apply')

    def to_json(self):
        return {
            'name':self.name,
            'stu_num':self.stu_num,
            'phone':self.phone,
            'email':self.email,
            'introduction':self.introduction,
            'skill':self.skill,
            'want_learn':self.want_learn,
            'think_celitea':self.think_celitea,
            'create_time':self.create_time.strftime('%Y-%m-%d'),
            'user_id':self.user_id
        }
