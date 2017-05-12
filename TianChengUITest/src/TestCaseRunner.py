#coding=utf8
#######################################################
#filename: TestCaseRunner.py
#author: defias
#date: 2016-4
#function: TestCaseRunner
#######################################################
import unittest, time, os
from Public import HTMLTestRunner, Function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def TestCaseRunner():
    '''运行测试用例'''
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    report_path =  Function.memdata.getvalue() + "\\Report\\testResult_TianchengUI_" + now + ".html" #测试报告存放路径
    fp = file(report_path, 'wb')
    report_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'天秤web测试报告', description=u'用例执行情况：' )

    test_dir = Function.memdata.getvalue() + "\\src\\TestCaseLib"  #测试用例存放路径
    test_list = unittest.defaultTestLoader.discover(test_dir, 'AutoTest*.py', test_dir)  #自动发现测试用例并生成测试套
    report_runner.run(test_list)
    fp.close()



if __name__ == '__main__':
    TestCaseRunner()
