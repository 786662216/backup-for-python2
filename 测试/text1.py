# coding:utf-8
# 重新封装，可以通过参数发不同的内容和调整时间

from weibo import APIClient
import time #可忽略
import datetime
import optparse
import random
import os

APP_KEY = '782542634' # app key
APP_SECRET = 'b5e3473a613bd8c740dc6b3b2d2a9550' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url

access_token = "2.00VfLpvC05FTxq9a86b1e3f5rjTuVC"
expires_in = 1660225135

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
client.set_access_token(access_token, expires_in)

print str(len('天下有两种人。一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留到最后吃。第一种人应该乐观，他每吃一颗都是吃剩的葡萄里最好的；第二种人应该悲观，他每吃一颗都是吃剩的葡萄里最坏的。不过事实却适得其反，第二种人还有希望，第一种人只有回忆。') // 2.6)


# client.statuses.share.post(status =  + 'http://www.google.com')
