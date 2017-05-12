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

#测试
if __name__ == '__main__':
    crd = Http_Custom_Request('http://192.168.18.77:8080/uap/api/ubas')
    headers = {"APPID":10, "TOKEN":"abcdefghijk"}
    crd.set_header(headers)
    data = '{"FunctionCode":"1003000003","MsgBody":{"result":{"message":"登录成功","result":"1","totalCount":0},"module":"UserApi","operateTime":"2015-08-21 10:49:24","param":{"RegistrationId":"010b8c44773","IP":"","userName":"13500000023","Latitude":"40.049246","Longitude":"116.296447","password":"**********","DevType":"Android","fromType":"3"},"tableName":"","userId":"4bcfa14b-0e33-4089-8fd7-3361d32f7eac","method":"PostUserLogin","ip":"192.168.1.88"},"CurrentTime":"2015-08-21 16:50:55"}}'
    r = crd.post(data)
    print r
    print r.status_code
    print r.headers
    print r.content

