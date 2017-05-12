#coding=utf8
#######################################################
#filename: ZHCreditPage.py
#author: defias
#date: 2016-3
#function: Main Page
#######################################################
from MainPage import MainPage
from time import sleep

class ZHCreditPage(MainPage):
    '''
    综合授信系统
    '''
    def __init__(self):
        super(ZHCreditPage, self).__init__()

    def PointCreditCredit(self):
        '''点击信用借授信'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-300']", 0)
        EleO.Click()
        return True

    def PointQuietCredit(self):
        '''点击悄悄借授信'''
        EleO = self.PO.FindElement("css", "a[data-parent='#menu-300']", 1)
        EleO.Click()
        return True

    def IntoCreditAnalysisPage(self):
        '''进入信用借授信分析'''
        selector = "a[href='/imp/a/ccs/creditLoan/creditStatistics']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointCreditCredit()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoCreditDailPage(self):
        '''进入信用借授信明细'''
        selector = "a[href='/imp/a/ccs/creditDetailModel']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointCreditCredit()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoWeidanbaoCreditDailPage(self):
        '''进入微担保授信明细'''
        selector = "a[href='/imp/a/ccs/weidanbaoDetailModel']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointCreditCredit()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True


    def IntoQuietCreditStatisticsPage(self):
        '''进入悄悄借授信分析'''
        selector = "a[href='/imp/a/ccs/creditLoan/quietCreditStatistics']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointQuietCredit()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoQuietCreditDetailPage(self):
        '''进入悄悄借授信明细'''
        selector = "a[href='/imp/a/ccs/quietCreditDetail']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointQuietCredit()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

#####################################################################################################################

class CreditAnalysisPage(object):
    '''
    信用借授信分析
    '''
    def __init__(self):
        self.PO = Page()

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class CreditDailPage(object):
    '''
    信用借授信明细
    '''
    def __init__(self):
        self.PO = Page()

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class WeidanbaoCreditDailPage(object):
    '''
    微担保授信明细
    '''
    def __init__(self):
        self.PO = Page()

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class QuietCreditStatisticsPage(object):
    '''
    悄悄借授信分析
    '''
    def __init__(self):
        self.PO = Page()

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class QuietCreditDetailPage(object):
    '''
    悄悄借授信明细
    '''
    def __init__(self):
        self.PO = Page()

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True
