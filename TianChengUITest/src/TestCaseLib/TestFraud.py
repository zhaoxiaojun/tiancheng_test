#coding=utf8
#######################################################
#filename: TestFraudDetail.py
#author: defias
#date: 2016-3
#function: TEST CASE
#######################################################
import unittest,time,os,sys
sys.path.append("..")
from Login import Login
from PageObject import *

class TestFraud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = 'http://192.168.18.77:8080/imp/a/login/'
        browser = 'firefox'
        cls.LoginO = Login()
        cls.LoginO.open(browser, url)  #打开页面

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.LoginO.login()  #登录

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.assertEqual(self.verificationErrors, [])
        self.LoginO.logout()  #登出

    @classmethod
    def tearDownClass(cls):
        cls.LoginO.close()  #关闭页面

    def test_Fraud_001(self):
        u'''反欺诈调用明细查询单个用户数据'''
        po = FraudPage.FraudDetailPage()
        po.InputUserInfo('15112526410')
        po.InputDate(u'全部')
        po.CkQuery()
        self.assertGreater(po.GetData(), 0)

    def test_Fraud_002(self):
        '''反欺诈调用明细查询全部数据'''
        po = FraudPage.FraudDetailPage()
        po.InputDate(u'全部')
        po.CkQuery()
        self.assertGreater(po.GetData(), 0)

    def test_Fraud_003(self):
        '''自助验证单个用户验证'''
        po = FraudPage.SelfHelpPage()
        po.InputUserName(u'袁伟伟')
        po.InputPhoneNumber('15112526410')
        po.InputCardNumber('420114198804164114')
        po.CkYanzheng()
        self.assertNotEqual(po.GetResultBorrowmoney(), '')

    def test_Fraud_004(self):
        '''预期智能预计查询'''
        po = FraudPage.IntelligentAlarmPage()
        po.InputBasicInfo('15112526410')
        po.CkQuery()
        self.assertNotEqual(po.QueryCheck(), '')

    def test_Fraud_005(self):
        '''正常查询用户聊天记录分析'''
        po = FraudPage.ChatLogsPage()
        po.InputBasicInfo('15112526410')
        po.CkQuery()
        self.assertNotEqual(po.QueryCheck(), '')

    def test_Fraud_006(self):
        '''正常查询手机通讯录分析'''
        po = FraudPage.PhoneAddressPage()
        po.InputBasicInfo('15112526410')
        po.CkQuery()
        self.assertEqual(po.QueryCheck(), '')

    def test_Fraud_007(self):
        '''用户地理位置跟踪查询用户基本信息'''
        po = FraudPage.UserLocationPage()
        po.InputBasicInfo('15112526410')
        po.CkQuery()
        self.assertEqual(po.QueryCheck(), '')

if __name__ == '__main__':
    #unittest.main()
    import sys
    from Public import HTMLTestRunner
    reload(sys)
    sys.setdefaultencoding('utf-8')

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = "testResult_TianchengUI_" + now + ".html"
    fp = file(report_path, 'wb')
    report_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'天秤UI测试报告', description=u'用例执行情况：')

    suite = unittest.TestSuite()
    suite.addTest(TestFraudDetail("test_Fraud_001"))
    suite.addTest(TestFraudDetail("test_Fraud_006"))
    suite.addTest(TestFraudDetail("test_Fraud_007"))
    report_runner.run(suite)
