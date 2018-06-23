#coding:utf-8
def SendWeibo(str):

    from weibo import APIClient

    APP_KEY = 'XXXXXXXXXX' # app key
    APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' # app secret
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url

    access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    expires_in = 1660225135

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)


    print client.statuses.share.post(status=str)
