import jwt
import time

secret = "8520"

def make_jwt(username,phone_num):
        payload = {
                "iss": "ccssbb.cn",
                "iat": int(time.time()),
                "exp": int(time.time()) + 86400 * 7,
                "username": username,
                "phone_num":phone_num,
        }
        token = jwt.encode(payload, secret, algorithm='HS256')
        return token

def verify_tokent(token):
        payload = {}
        try:
                payload = jwt.decode(token, secret, algorithms='HS256')
        except:
                pass
        return payload