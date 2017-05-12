#coding=utf8
#######################################################
#filename:Custom_Server_IMTongxlu.py
#author:defias
#date:2015-9
#function: http server
#######################################################
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingTCPServer
import threading
import urllib
import json

class Custom_HTTPRequestHandler(BaseHTTPRequestHandler):
    def _getdata(self, path, params):
        '''Get response data'''
        print 'request params: ', params
        if '/txlService/api/sync-mobile-contacts' != path:
            return None
        if 'favicon.ico' != params:
            params = '{"' + params + '"}'
            params_jsonstr = params.replace('=','":"').replace('&','","')
            params_dic = json.loads(params_jsonstr)
            functioncode = params_dic['FunctionCode']
            if ('1005000001' != functioncode):
                return None
        #读取json文件数据
        datafile = 'response_data_IMTongxlu.json'
        datafp = open(datafile, 'r')
        data = datafp.read()
        response_data = "".join(data.split())
        return response_data


    def _writeheader(self, data):
        '''Write header'''
        if data is None:
            self.send_response(404)
        else:
            self.send_response(200)
        self.send_header('Content-Type','text/plain;charset=utf-8')
        self.end_headers()

    def do_GET(self):
        '''Handle get request'''
        print "Handling with thread: ", threading.currentThread().getName()
        print 'got connection from ',self.client_address

        #解析请求参数
        path_list = self.path.split('?')
        request_params = path_list[-1]
        request_path = path_list[0]

        data = self._getdata(request_path, request_params)
        self._writeheader(data)
        if data is None:
            self.wfile.write('None')
        else:
            self.wfile.write(data)

#启动服务
def Start_Server():
    try:
        print 'server is running....'
        httpd_address = ('192.168.10.93', 5555)
        myhttpd = ThreadingTCPServer(httpd_address, Custom_HTTPRequestHandler)
        myhttpd.serve_forever()

    except KeyboardInterrupt:
        myhttpd.socket.close()

if __name__ == '__main__':
    Start_Server()
