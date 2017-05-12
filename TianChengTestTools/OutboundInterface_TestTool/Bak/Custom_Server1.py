#coding=utf8
#######################################################
#filename:Http_Custom_Server.py
#author:defias
#date:2015-8
#function:
#######################################################
import socket
import urllib
import json
RECV_LEN = 4096  #接收请求数据长度
MAX_CONN = 100   #最大连接数

#server code
class Http_Custom_Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    #设置响应体
    def set_data(self, data=''):
        reg_content = '''
HTTP/1.1 200 ok
Content-Type:text/plain;charset=utf-8

'''
        self.response_content = reg_content + data  # 待响应发送数据

    def start_server(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.host, self.port))
            sock.listen(MAX_CONN)  # 监听
            print 'http server %s:%d is  listening... ' % (self.host,self.port)

            self.conn, addr = sock.accept()  # 接收客户端连接
            print 'http server accepted, addr:%s' % str(addr)

            self.request = self.conn.recv(RECV_LEN) # 接收数据
            print 'request is:', self.request
            return True
        except:
            print 'http server exception!'
            return False

    def send_response(self):
        try:
            #print self.response_content
            #self.response_content = self.response_content.encode('utf-8')
            self.conn.sendall(self.response_content)
            #self.conn.close()
            return True
        except:
            print 'send response exception!'
            return False



def read_data(filename):
    f = open(filename, 'r')
    s = f.read()
    u = s.decode('utf-8')  #从utf8转为unicode
    r = u.encode('gbk')  #从unicode转为utf8
    #k = json.loads(s)
    m = json.dumps(r)
    #print m
    return m
\

def main(host,port,request_path,request_params,response_filename):
    testhttpd = Http_Custom_Server(host,port)
    testhttpd.set_header()

    #response_data = read_data(response_filename)
    response_data = '{"ReturnCode":0,"Message":"成功！","FunctionCode":"1001000001","CurrentTime":"20150821110218068005","TotalNum":14897,"DataList":{"UserBasicInfo":{"Age":"","CardAddress":"","CardType":1,"GuaranteeLever":"","NickName":"13230005176","RealName":"test","RegisterTime":"20150415210610000003","Sex":0,"TelNo":"13230005176","UserAccount":"","UserId":"1498666e-c3d2-4692-a760-95dbe2295614","UserStatus":1,"UserType":1}},"SessionId":"91368f7b-d6ea-4d23-b542-c08cdc8c29d2"}'
    testhttpd.set_data(response_data)

    testhttpd.start_server()
    if check_request(testhttpd,request_path,request_params):
        testhttpd.send_response()
    else:
        print '请求参数错误！'
