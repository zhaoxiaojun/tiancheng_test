#coding=utf8
#######################################################
#filename:Custom_SynServer.py
#author:defias
#date:2015-9
#function: http server
#######################################################
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingTCPServer
import threading
import urllib
import json
import sys,getopt
import configparser

def Custom_SynServer(vhost, vport, vfunctioncode, vdatafile):
    class Custom_HTTPRequestHandler(BaseHTTPRequestHandler):
        def _getdata(self, path, params):
            '''Get response data'''
            print 'request params: ', params
            if '/niiwoo-open-api/openApiController/' != path:
                return None
            if 'favicon.ico' != params:
                params_dic = json.loads(params)
                functioncode = params_dic['FunctionCode']
                if (vfunctioncode != functioncode):
                    return None
            #读取json文件数据
            datafile = vdatafile
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
            path_list = self.path.split('/')
            request_params_url = path_list[-1]
            request_path = self.path.replace(request_params_url, '')
            request_params = urllib.unquote(request_params_url)

            data = self._getdata(request_path, request_params)
            import time
            print 'sleep...'
            time.sleep(30)

            self._writeheader(data)
            if data is None:
                self.wfile.write('None')
            else:
                self.wfile.write(data)

    class Custom_HTTPRequestHandler_IMTongxlu(BaseHTTPRequestHandler):
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
                if (vfunctioncode != functioncode):
                    return None
            #读取json文件数据
            datafile = vdatafile
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
            import time
            time.sleep(30)

            self._writeheader(data)
            if data is None:
                self.wfile.write('None')
            else:
                self.wfile.write(data)

    try:
        httpd_address = (vhost, int(vport))
        if '1005000001' == vfunctioncode:
            myhttpd = ThreadingTCPServer(httpd_address, Custom_HTTPRequestHandler_IMTongxlu)
            print "server:IMTongxlu"
        else:
            myhttpd = ThreadingTCPServer(httpd_address, Custom_HTTPRequestHandler)
        print 'server is running....'
        myhttpd.serve_forever()

    except KeyboardInterrupt:
        myhttpd.socket.close()


if __name__ == '__main__':
    def usage():
        print 'usage: '
        print sys.argv[0] + ' -h host/ip -p port -c functioncode -f datafile'
        print sys.argv[0] + ' --host=host/ip --port=port  --code=functioncode  --file=datafile'
        print sys.argv[0] + ' --help'

    num_args = len(sys.argv) - 1
    #获取命令行参数
    if num_args != 0:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:c:f:", ["help", "host=", "port=", "code=", "file="])
        for op, value in opts:
            if (op=='-h') or (op=='--input'):
                host = value
            elif (op=='-p') or (op=='--port'):
                port = value
            elif (op=='-c') or (op=='--code'):
                functioncode = value
            elif (op=='-f') or (op=='--file'):
                datafile = value
            elif op=='--help':
                usage()
                sys.exit()
        print "host port functioncode datafile: ",host,port,functioncode,datafile

    else:
        #读配置文件
        config = configparser.ConfigParser()
        config.read(".\\Custom_SynServer.ini")

        host = str(config.get('DEFAULT', 'host'))
        port = str(config.get('DEFAULT', 'port'))
        functioncode = str(config.get('DEFAULT', 'functioncode'))
        datafile = str(config.get('DEFAULT', 'datafile'))
        print "host port functioncode datafile: ",host,port,functioncode,datafile

    #启动服务
    Custom_SynServer(host, port, functioncode, datafile)
