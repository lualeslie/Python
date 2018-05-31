# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 第三方 SMTP 服务
mail_host="smtp.163.com"  # 设置服务器
mail_user="****"    # 用户名
mail_pass="****"   # 口令

sender = '****'
receivers = ['****']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart()
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message['From'] = "{}".format(sender)  # 发送者
message['To'] = ",".join(receivers)  # 接收者
message['Subject'] = 'Python SMTP 邮件测试'

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

# html格式加图片
email_msg =  """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">百度</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
message.attach((MIMEText(email_msg, 'html', 'utf-8')))
fp = open('monkey.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    # smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())     # 发送
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
