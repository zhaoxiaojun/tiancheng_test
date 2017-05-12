#coding=utf8
#######################################################
#filename: TestCase.py
#author: defias
#date: 2016-3
#function: TEST CASE
#######################################################
import unittest,time,os,sys
sys.path.append("..")
from PageObject import IndexPage
from Login import Login

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.LoginO = Login()
        cls.LoginO.open()  #打开页面

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.assertEqual(self.verificationErrors, [])

    @classmethod
    def tearDownClass(cls):
        cls.LoginO.close()  #关闭页面

    def test_login_success_001(self):
        '''正常登录登出'''
        po = IndexPage.IndexPage()
        po.InputUser('root')
        po.InputPasswd('root123')
        po.CkLoginButton()
        self.assertEqual(u'您好, 超级管理员 ', po.LoginSucessCheck())
        po.Logout()


if __name__ == '__main__':
    unittest.main()


