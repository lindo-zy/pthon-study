#python3   发送邮件
import smtplib
#创建SMTP对象
'''
smtpObj=smtplib.SMTP( [host [, port [, local_hostname]]] )
host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。
'''
#发送邮件
'''
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息
'''
from email.mime.text import MIMEText
from email.header import Header
sender='test@pythob.com'
receiver=['492201845@qq.com']
message=MIMEText('python 邮件发送测试...','plain','utf-8')
message['From']=Header('zy','utf-8')
message['To']=Header('测试','utf-8')

subject='Python 邮件测试'
message['Subject']=Header(subject,'utf-8')
try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receiver,message.as_string())
    print('发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')
