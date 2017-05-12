#coding=utf8
#######################################################
#filename: TianchengPage.py
#author: defias
#date: 2016-3
#function: Tiancheng Web Page
#######################################################
from Page import Page

class IndexPage(object):
    '''
    天秤首页
    '''
    def __init__(self):
        self.PO = Page()

    def Open(self, browser, url):
        '''打开天秤首页'''
        self.PO.OpenUrl(browser, url)
        return True

    def InputUser(self,user):
        '''输入用户名'''
        EleO = self.PO.FindElement("id", "username")
        EleO.Input(user)
        return True

    def InputPasswd(self,passwd):
        '''输入密码'''
        EleO = self.PO.FindElement("id", "password")
        EleO.Input(passwd)
        return True

    def CkJZWCheckBox(self):
        '''勾选记住我'''
        EleO = self.PO.FindElement("id", "rememberMe")
        EleO.Click()
        return True

    def CkLoginButton(self):
        '''点击登录按钮'''
        EleO = self.PO.FindElement("class", "login_btn")
        EleO.Click()
        return True

    def Close(self):
        '''关闭浏览器'''
        self.PO.CloseBrowser()
        delattr(self.PO, 'driverO')
        return True

    def Logout(self):
        '''登出'''
        self.PO.SwithToFrame()
        EleO = self.PO.FindElement("css", "a[onclick='logoutOrExit()']")
        EleO.Click()
        return True

    def LoginSucessCheck(self):
        '''登录成功检查点'''
        self.PO.SwithToFrame()
        EleO = self.PO.FindElement("class", 'dropdown-toggle')
        return EleO.GetText()


