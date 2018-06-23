#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '549670951@qq.com'  # 发件人邮箱账号
my_pass = 'kjisqtpjlpxfbgae'  # 发件人邮箱密码
my_user = '786662216@qq.com'  # 收件人邮箱账号

def mail():
    try:
        msg = MIMEText('python:helloworld', 'plain', 'utf-8')
        msg['From'] = formataddr(["OLDshe-server", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["OLDshe-client", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的加密SMTP服务器，端口是465或587
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print('邮件发送成功')
    except Exception:
        print('邮件发送失败')

