import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

db_keys = db.keys()

def md5(char):
    md5 = hashlib.md5()
    md5.update(char)
    return md5.hexdigest()

def login(username,password):
    for user in db:
        if user in db_keys:
            if username == db_keys[db_keys.index(user)]:
                if (md5(password) == db[user]):
                    print "user confirmed"
                    return True
    print "username or password are wrong"
    return False

login('michael','123456')