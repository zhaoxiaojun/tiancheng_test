#coding=utf8
#######################################################
#filename: Login.py
#author: defias
#date: 2016-3
#function: login web site
#######################################################
import unittest,time,os,sys
sys.path.append(os.environ['TCWT_HOME'] + '\\src\\')
from PageObject import IndexPage


class Login(object):
    def __init__(self):
        self.po = IndexPage.IndexPage()

    def open(self, browser, url):
        '''打开天秤登录页面'''
        self.po.Open(browser, url)

    def login(self):
        '''登入'''
        self.po.InputUser('root')
        self.po.InputPasswd('root123')
        self.po.CkLoginButton()

    def logout(self):
        '''登出'''
        self.po.Logout()

    def close(self):
        '''关闭页面'''
        self.po.Close()

if __name__ == '__main__':
    LoginO = Login()
    LoginO.open()
    LoginO.login()
    LoginO.logout()
    LoginO.close()
