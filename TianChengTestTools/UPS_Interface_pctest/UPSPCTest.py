#coding=utf8
#######################################################
#filename:Http_Custom_Request.py
#author:defias
#date:2015-7
#function:
#######################################################
from Global import *
from GenerateLog import GenerateTxtLog
import threading
import Queue
import time


def UPSPCTest():
    '''
    测试主流程
    '''
    #启动日志
    GenerateTxtLog.GenTxtLog()

    #锁
    tresult_qlock = threading.Lock()

    #全局变量
    global testcase_result
    global taskassert_queue

    #记录测试开始时间
    start_time = getnowstamp()
    start_now = getnowtime()
    PrintLog('debug', '测试开始时间: %s', start_now)

    #获取待执行用例
    TestIds = getModTestid(runmode)
    PrintLog('debug', '待执行用例: %s', TestIds)

    #启动执行子线程
    PrintLog('debug', 'Starting thread: TestRunThread')
    Thread_runO = TestRunThread('TestRunThread', tresult_qlock, TestIds)
    Thread_runO.setDaemon(True)
    Thread_runO.start()
    time.sleep(1)

    #启动断言子线程
    PrintLog('debug', 'Starting thread: TestAssertThread')
    Thread_assertO = TestAssertThread('TestAssertThread', tresult_qlock)
    Thread_assertO.setDaemon(True)
    Thread_assertO.start()


    #等待断言子线程结束
    PrintLog('debug', '等待子线程TestRunThread结束...')
    Thread_runO.join()
    PrintLog('debug', '子线程：TestRunThread结束')

    PrintLog('debug', '等待子线程TestAssertThread结束...')
    Thread_assertO.join()
    PrintLog('debug', '子线程：TestAssertThread结束')

    #等待任务队列为空
    #taskassert_queue.join()

    #测试结束时间
    end_time = getnowstamp()
    end_now = getnowtime()
    PrintLog('debug', '测试结束时间: %s', end_now)

    #生成测试报告
    PrintLog('debug', 'testcase_result: %s', testcase_result)
    HtmlReportO = HtmlReport(testcase_result, end_time-start_time)
    HtmlReportO.generate_html()
