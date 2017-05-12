#coding=utf8
#######################################################
#filename:Http_Custom_Request.py
#author:defias
#date:2015-7
#function:
#######################################################
import requests
import json

#http请求类
class Http_Custom_Request(object):
    '''用于封装http请求方法'''
    def __init__(self, url):
        self.url = url
        self.headers = {}  #http头

    #设置http头
    def set_header(self, headers):
        self.headers = headers

    #封装HTTP GET请求方法
    def get(self, *params):
        params_n = len(params)
        try:
            if 0 == params_n:
                response = requests.get(self.url, headers=self.headers)
            elif 1 == params_n:
                response = requests.get(self.url, params=params[0], headers=self.headers)
            else:
                print('params is error!')
                raise
            return response
        except Exception:
            print('requests exception')
            return -1

    #封装HTTP POST请求方法
    def post(self, *data):
        data_n = len(data)
        try:
            if 0 == data_n:
                response = requests.post(self.url, headers=self.headers)
            elif 1 == data_n:
                response = requests.post(self.url, data=data[0], headers=self.headers)
            else:
                print('data is error!')
                raise
            return response
        except Exception:
            print('requests exception')
            return -1


    #扩展封装HTTP xxx请求方法

if __name__ == '__main__':
    crd = Http_Custom_Request('http://192.168.18.33:8080/uap/ubas/api')
    headers = {"APPID":10, "TOKEN":"abcdefghijk"}
    crd.set_header(headers)
    data = '{"FunctionCode":"1003000009","MsgBody":{"result":{"message":"证件号已存在","result":"-1","totalCount":0},"module":"UserApi","operateTime":"2015-08-12 10:25:58","param":{"Idcard":"513029198912164289","UserId":"13091cae-618f-4cdd-b486-c5e0c16c7a8f","RealName":"健康快乐"},"tableName":"","userId":"13091cae-618f-4cdd-b486-c5e0c16c7a8f","method":"PostConfirmRealName","ip":"218.6.111.161"},"CurrentTime":"2015-08-12 10:32:24"}'
    r = crd.post(data)
    print r
    print r.status_code
    print r.headers
    print r.content

