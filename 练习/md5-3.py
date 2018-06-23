#coding:utf-8
#加盐的登录
import hashlib

db = {
    'michael': '123456',
    'bob': 'abc999',
    'alice': '888888'
}

db_keys = db.keys()

# 生成MD5
def safe_md5(username,password):
    salt = 'the-Salt'
    md5 = hashlib.md5()
    md5.update(username + password + salt)
    return md5.hexdigest()

dbmd5 = []

for key in db:
    dbmd5.append(safe_md5(key,db[key]))

# 安全登录
def safe_login(username,password):
    for user in db:
        if user in db_keys:
            if username == db_keys[db_keys.index(user)]:
                if (safe_md5(username,password) in dbmd5):
                    print "user confirmed"
                    return True
    print "username or password are wrong"
    return False

safe_login('michael','123456')