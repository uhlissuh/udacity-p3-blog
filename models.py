from google.appengine.ext import db
import security

class BlogPost(db.Model):
    subject = db.StringProperty(required = True)
    content = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class User(db.Model):
    username = db.StringProperty(required = True)
    email = db.StringProperty()
    password_hash = db.StringProperty(required = True)

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        return User.all().filter('username =', name).get()


    @classmethod
    def register(cls, username, password, email = None):
        pw_hash = security.make_password_hash(username, password)
        return User(username = username,
                    password_hash = pw_hash,
                    email = email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and security.valid_pw(name, pw, u.pw_hash):
            return u
