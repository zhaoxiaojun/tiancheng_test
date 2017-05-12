#coding=utf8
#######################################################
#filename:Http_Custom_Server.py
#author:defias
#date:2015-9
#function:
#######################################################
import urllib
import json
from SocketServer import (StreamRequestHandler as SRH, ThreadingTCPServer as TTCPS)
from time import ctime

class Custom_Server(object):
    #设置服务器ip和port
    def __init__(self, host, port):
        self.host = host
        self.port = port

    #设置服务器响应
    def set_response_data(self, response_data=''):
        self.response_data = response_data

    #自定义处理器
    class Http_Server_Handler(SRH):

        def handle(self):
            #客户端ip和port
            print 'got connection from ',self.request.getpeername()
            #print 'got connection from ',self.client_address

            #客户端请求数据
            print 'client request data:\n',self.request.recv(1024)
            #print 'client request data:\n',self.rfile.readline()

            #发送响应
            print 'response_data is:\n',self.outself.response_data
            self.request.sendall('connection %s:%s at %s succeed!\n' % (host,port,ctime()))
            self.request.sendall('Thank you for connecting\n')
            #self.wfile.write('connection %s:%s at %s succeed!\n' % (host,port,ctime()))
            #self.wfile.write('Thank you for connecting\n')

    #启动服务
    def Start_Server(self):
        print 'server is running....'
        addr = (self.host,self.port)
        server = TTCPS(addr,self.Http_Server_Handler())
        server.serve_forever()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5555
    Custom_Server_O = Custom_Server(host,port)
    Custom_Server_O.set_response_data('hello world!')
    Custom_Server_O.Start_Server()
