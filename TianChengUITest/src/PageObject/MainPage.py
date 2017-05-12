#coding=utf8
#######################################################
#filename: MainPage.py
#author: defias
#date: 2016-3
#function: Main Page
#######################################################
from Page import Page


class MainPage(object):
    '''
    登录后的主页面
    '''
    def __init__(self):
        self.PO = Page()

    def CloseFristTab(self):
        loc_type = "css"
        loc_value = ".tab_close>a"
        if self.PO.isPresent(loc_type, loc_value):
            self.PO.FindElement(loc_type, loc_value).Click()
        return True

    def IntoFraudPage(self):
        '''反欺诈平台'''
        self.PO.FindElement("css", "a[data-id='100']").Click()
        self.CloseFristTab()
        return True

    def IntoUserBehaviorPage(self):
        '''用户行为分析系统'''
        self.PO.FindElement("css", "a[data-id='400']").Click()
        self.CloseFristTab()
        return True

    def IntoUpsSysPage(self):
        '''用户画像系统'''
        self.PO.FindElement("css", "a[data-id='500']").Click()
        self.CloseFristTab()
        return True

    def IntoYunyinPage(self):
        '''运营决策平台'''
        self.PO.FindElement("css", "a[data-id='600']").Click()
        self.CloseFristTab()
        return True

    def IntoZHCreditPage(self):
        '''综合授信系统'''
        self.PO.FindElement("css", "a[data-id='300']").Click()
        self.CloseFristTab()
        return True

    # def IntoPersonInfoPage(self):
    #     '''个人信息'''
    #     EleO = self.FindElement("css", "a[href='/imp/a/sys/user/info']")
    #     return Ele(EleO).Click()

    # def IntoChangePasswdPage(self):
    #     '''修改密码'''
    #     EleO = self.FindElement("css", "a[href='/imp/a/sys/user/modifyPwd']")
    #     return Ele(EleO).Click()



