#socket模块 网络编程
import socket
import sys
'''
socket.socket([family[, type[, proto]]])
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.
'''

#服务器端套接字
'''
s.bind()    绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
s.listen()  开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
s.accept()  被动接受TCP客户端连接,(阻塞式)等待连接的到来
'''

#客户端套接字
'''
s.connect() 主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

'''
#公用套接字
'''
s.recv()    接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量
s.send()    发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小
s.sendall() 完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
s.recvform() 接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
s.sendto()  发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数
s.close()   关闭套接字
s.getpeername() 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
s.getsockname() 返回套接字自己的地址。通常是一个元组(ipaddr,port)
s.setsockopt(level,optname,value)   设置给定套接字选项的值。
s.getsockopt(level,optname,value)   返回定套接字选项的值。
s.settimeout(timeout)   置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
s.gettimeout()          返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
s.fileno()      返回套接字的文件描述符。
s.makefile()    创建一个与该套接字相关连的文件

'''
#服务端
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
serversocket.bind((host,port))
serversocket.listen(5)
while True:
    clientsocket,addr=serversocket.accept()
    print('连接地址:%s'%str(addr))
    msg='欢迎访问!'+'\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
#客户端
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.connect((host,port))
msg=s.recv(1024)
s.close()
print(msg.decode('utf-8'))


#python Internet模块
'''
HTTP   网页访问           端口80      urllib
NNTP   阅读和张贴新闻     端口119     nntplib
FTP    文件传输           端口20      ftplib，urllib
SMTP   发送邮件           端口25      smtplib
POP3   接受邮件           端口110     poplib
IMAP4  获取邮件           端口143     imaplib
'''