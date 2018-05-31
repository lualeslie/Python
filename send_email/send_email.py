# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import random

def generate_verification_code():
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素
    verification_code = ''.join(myslice)  # list to string
    return verification_code

# 第三方 SMTP 服务
mail_host="smtp.163.com"  # 设置服务器
mail_user="****"    # 用户名
mail_pass="****"   # 口令

sender = '****'
receivers = ['****']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
code = generate_verification_code()
mail_msg = "<html><p>测试验证码，验证码为：{0}. </p></html>".format(code)
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = "{}".format(sender)  # 发送者
message['To'] = ",".join(receivers)  # 接收者
message['Subject'] = 'Python SMTP 邮件测试'

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    # smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())     # 发送
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
