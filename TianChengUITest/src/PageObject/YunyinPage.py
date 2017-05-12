#coding=utf8
#######################################################
#filename: YunyinPage.py
#author: defias
#date: 2016-3
#function: Main Page
#######################################################
from MainPage import MainPage
from time import sleep

class YunyinPage(object):
    '''
    运营决策平台
    '''
    def __init__(self):
        self.PO = Page()

    def PointUserUPS(self):
        '''点击精细化运营'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-600']", 0)
        EleO.Click()
        return True

    def PointUserLabel(self):
        '''点击信用借业务分析'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-600']", 1)
        EleO.Click()
        return True

    def PointLabelLibManage(self):
        '''点击悄悄借业务分析'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-600']", 2)
        EleO.Click()
        return True

    def PointWorkplanManage(self):
        '''点击活动专题'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-600']", 3)
        EleO.Click()
        return True

    def IntoUPSBeta(self):
        '''进入运营展示大屏幕'''
        selector = "a[href='/imp/a/odp/screenScheme']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserUPS()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoFetchUserPage(self):
        '''进入资金流水监控'''
        selector = "a[href='/imp/a/odp/marketing/listCurFundDetail?map.tabtype=realTimeMonitoring']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserLabel()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoLabelManagePage(self):
        '''进入启动次数分析'''
        selector = "a[href='/imp/a/odp/marketing/listClientVersionDistribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointLabelLibManage()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoWorkplanManagePage(self):
        '''进入计划任务管理'''
        selector = "a[href='/imp/a/ups/scheduleJob']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointWorkplanManage()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

#####################################################################################################################
