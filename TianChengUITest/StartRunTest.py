#coding=utf8
#######################################################
#filename:StartRunTest.py
#author:defias
#date:2016-4
#function: 测试启动
#######################################################
from src import TestCaseGenerator, TestCaseRunner, Public
import time


def StartRunTest():
    print 'TianchengUITest RunStart...'
    Public.Function.DealEnviron()
    TestCaseGenerator.Run()
    time.sleep(3)
    TestCaseRunner.TestCaseRunner()

if __name__ == '__main__':
    StartRunTest()
