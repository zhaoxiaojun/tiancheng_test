#coding=utf8
#######################################################
#filename:Custom_Server_TuandaiCCS.py
#author:defias
#date:2015-9
#function: http server
#######################################################
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingTCPServer
import urllib
import json
import MySQLdb
import sys,getopt
import re
from Configfile_Parser import Configfile_Parser

class Custom_HTTPRequestHandler(BaseHTTPRequestHandler):
    print 234
    def do_POST(self):
        '''Handle post request'''
        print 'got connection from ',self.client_address

        #解析请求参数
        path_list = self.path.split('?')
        request_params = path_list[-1]
        request_path = path_list[0]

        print 'get data!'
        data = self._getdata(request_path, request_params)
        print 'write data'
        self._writedata(data)

    def _getdata(self, path, params):
        '''Post response data'''
        print 'request path: ', path
        print 'request params: ', params

        params = urllib.unquote(params)
        if 'favicon.ico' == params:
            post_interface = 'None'
        elif '/NiwoPassport/PostGetUserIdByMobile' == path:
            post_interface = 'GetUserIdByMobile'
        elif '/UserMoney/PostUserStatistMoneyInfo' == path:
            post_interface = 'UserStatistMoneyInfo'
        elif '/Common/PostUserInfoNew' == path:
            post_interface = 'UserInfoNew'
        else:
            post_interface = 'None'

        print 'post_interface: ',post_interface
        if post_interface not in ['GetUserIdByMobile','UserStatistMoneyInfo','UserInfoNew']:
            return None
        jsonString = params.split('&')[0]
        jsonStringvalues = jsonString.split('=')[-1]
        jsonStringlist = json.loads(jsonStringvalues)

        #读配置文件
        mobile_vardata_conf = Configfile_Parser(".\\Custom_Server_TuandaiCCS.ini")
        mobile_vardata = mobile_vardata_conf.get_index()
        #print 'mobile_vardata: ',mobile_vardata
        #mobile_vardata = {'131':(0,5000,0), '132':(0,10000,0), '133':(0,50000,0), '134':(0,100000,0), '135':(0,100001,0), '136':(1,5000,1000), '137':(1,10000,1000), '138':(1,50000,1000), '139':(1,100000,1000), '140':(1,100001,1000), '141':(2,5000,1000), '142':(2,10000,1000), '143':(2,50000,1000), '144':(2,100000,1000), '145':(2,100001,1000), '146':(3,5000,1000), '147':(3,10000,1000), '148':(3,50000,1000), '149':(3,100000,1000), '150':(3,100001,1000), '151':(3,100001,60000)}
        #CCS1
        if post_interface == 'GetUserIdByMobile':
            response_list = {}
            userMobile = jsonStringlist['userMobile']
            #userid = self._querydb_getdata(userMobile)  #查数据库得到userid
            userid = userMobile  #将userMobile作为userid返回
            print 'response data:', userid
            response_list['userId'] = userid
            response_jsonstr =  json.dumps(response_list)

        #CCS2
        elif post_interface == 'UserStatistMoneyInfo':
            response_jsonstr = '{"FirstLoanDate":"","TotalLoanCount":0,"TotalLoanMoney":0,"DelayTotalCount":0,"DelayToalMoney":0,"WaitReturnMoney":0,"FirstInvestDate":"","TotalInvestCount":0,"TotalInvestMoney":0,"RecentOneYearAvgInvestCount":0,"RecentOneYearAvgInvestMoney":0,"RecentOneYearInvestCount":0,"RecentOneYearInvestMoney":0,"RecentOneYearAvgInvestDeadline":0,"DueinTotalMoney":0,"DueinTotalDay":0,"ArgDueinMoney":0,"AviMoney":0,"DueinPlusAviMoney":0,"ReturnCode":1,"ReturnMessage":"成功","UserId":"3c90ae9a-d45e-447c-80af-3c2078ab5f48","UserName":"wal398139444","IDCardNo":"43052519861228611X","TuanDaiUserType":2}'
            response_dic = json.loads(response_jsonstr)

            userid = jsonStringlist['UserId']
            #userMobile = self._querydb_getdata(userid) #查数据库得到userMobile
            userMobile = userid

            RecentOneYearTotalLoanCount = mobile_vardata[userMobile][0]
            RecentOneYearTotalLoanMoney = mobile_vardata[userMobile][1]
            print 'response data:', RecentOneYearTotalLoanCount, RecentOneYearTotalLoanMoney

            response_dic['RecentOneYearTotalLoanCount'] = RecentOneYearTotalLoanCount
            response_dic['RecentOneYearTotalLoanMoney'] = RecentOneYearTotalLoanMoney
            response_jsonstr = json.dumps(response_dic)

        #CCS3
        elif post_interface == 'UserInfoNew':
            response_jsonstr = '{"accountAmount":0,"recoverBorrowOut":0,"recoverDueOutPAndI":0,"status":"00","desc":""}'
            response_dic = json.loads(response_jsonstr)

            userid = jsonStringlist['UserId']
            #userMobile = self._querydb_getdata(userid)  #查数据库得到userMobile
            userMobile = userid

            AvgDayDueInMoneyOneYear = mobile_vardata[userMobile][2]
            print 'response data:',  AvgDayDueInMoneyOneYear

            response_dic['AvgDayDueInMoneyOneYear'] = AvgDayDueInMoneyOneYear
            response_jsonstr = json.dumps(response_dic)

        else:
            return None

        return response_jsonstr

    # def _querydb_getdata(self, param):
    #     conn = MySQLdb.connect(host='192.168.18.69',user='root',passwd='niiwooroot',port=3306)  #连接数据库
    #     conn.select_db('ubas_tianchengtest')  #选择数据库
    #     cur = conn.cursor()
    #     pattern = re.compile(r'\w+-\w+')  #匹配userid
    #     match = pattern.match(param)
    #     if match:
    #         count = cur.execute("SELECT MobilePhone FROM userbasicinfo WHERE UserId = %s", (param,))
    #     else:
    #         count = cur.execute("SELECT UserId FROM userbasicinfo WHERE MobilePhone = %s", (param,))
    #     result = cur.fetchone()
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #     return result[0]

    def _writedata(self, data):
        '''Write header'''
        if data is None:
            self.send_response(404)
            self.send_header('Content-Type','text/plain;charset=utf-8')
            self.end_headers()
            self.wfile.write('None')
        else:
            self.send_response(200)
            self.send_header('Content-Type','text/plain;charset=utf-8')
            self.end_headers()
            self.wfile.write(data)

#启动服务
def Start_Server(host, port):
    try:
        print 'server is running....'
        httpd_address = (host, int(port))
        myhttpd = ThreadingTCPServer(httpd_address, Custom_HTTPRequestHandler)
        #myhttpd = HTTPServer(httpd_address, Custom_HTTPRequestHandler)
        print 'myhttpd:', myhttpd
        myhttpd.serve_forever()

    except KeyboardInterrupt:
        print 11111111111
        print 'myhttpd:', myhttpd
        #myhttpd.socket.close()
        myhttpd.shutdown
        print 22222222222


if __name__ == '__main__':
    def usage():
        print 'usage: '
        print sys.argv[0] + ' -h host/ip -p port'
        print sys.argv[0] + ' --host=host/ip --port=port'
        print sys.argv[0] + ' --help'

    opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["help", "host=", "port="])
    for op, value in opts:
        if (op=='-h') or (op=='--input'):
            host = value
        elif (op=='-p') or (op=='--port'):
            port = value
        elif op=='--help':
            usage()
            sys.exit()

    Start_Server(host, port)
