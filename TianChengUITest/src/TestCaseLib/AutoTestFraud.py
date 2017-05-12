#coding=utf8
#######################################################
#filename: AutoTestFraud.py
#author: TestCaseGenerator
#date: 2016-04-22 14:50:12
#function: unittest test case
#######################################################
import unittest,time,os,sys
sys.path.append(os.environ['TCWT_HOME'] + '\\src\\')
from Login import Login
from PageObject import *


class TestFraud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = 'http://192.168.18.77:8080/imp/a/login'
        browser = 'firefox'
        cls.LoginO = Login()
        cls.LoginO.open(browser, url)  #open web page

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.LoginO.login()  #login

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.assertEqual(self.verificationErrors, [])
        self.LoginO.logout()  #logout

    @classmethod
    def tearDownClass(cls):
        cls.LoginO.close()  #close web page

    def test_Fraud_tc1(self):
        u'''反欺诈调用明细查询单个用户数据'''
        po = FraudPage.FraudDetailPage()
        po.InputUserInfo(u'15112526410')
        po.InputDate(u'全部')
        po.CkQuery()
        self.assertGreater(po.GetData(), 0)

    def test_Fraud_tc2(self):
        u'''反欺诈调用明细查询全部数据'''
        po = FraudPage.FraudDetailPage()
        po.InputDate(u'全部')
        po.CkQuery()
        self.assertGreater(po.GetData(), 0)

    def test_Fraud_tc3(self):
        u'''自助验证单个用户验证'''
        po = FraudPage.SelfHelpPage()
        po.InputUserName(u'袁伟伟')
        po.InputPhoneNumber(u'15112526410')
        po.InputCardNumber(u'420114198804164114')
        po.CkYanzheng()
        self.assertNotEqual(po.GetResultBorrowmoney(), "")

    def test_Fraud_tc4(self):
        u'''预期智能预计查询'''
        po = FraudPage.IntelligentAlarmPage()
        po.InputBasicInfo(u'15112526410')
        po.CkQuery()
        self.assertNotEqual(po.QueryCheck(), "")

    def test_Fraud_tc5(self):
        u'''正常查询用户聊天记录分析'''
        po = FraudPage.ChatLogsPage()
        po.InputBasicInfo(u'15112526410')
        po.CkQuery()
        self.assertEqual(po.QueryCheck(), "")

    def test_Fraud_tc6(self):
        u'''正常查询手机通讯录分析'''
        po = FraudPage.PhoneAddressPage()
        po.InputBasicInfo(u'15112526410')
        po.CkQuery()
        self.assertEqual(po.QueryCheck(), "")

    def test_Fraud_tc7(self):
        u'''用户地理位置跟踪查询用户基本信息'''
        po = FraudPage.UserLocationPage()
        po.InputBasicInfo(u'15112526410')
        po.CkQuery()
        self.assertEqual(po.QueryCheck(), "")
