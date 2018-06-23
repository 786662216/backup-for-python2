import hashlib
def md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()
print md5('123456')