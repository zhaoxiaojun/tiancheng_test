#coding=utf8
#######################################################
#filename: UpsSysPage.py
#author: defias
#date: 2016-3
#function:Ups Sys Page
#######################################################
from MainPage import MainPage
from time import sleep

class UpsSysPage(MainPage):
    '''
    用户画像系统
    '''
    def __init__(self):
        super(FraudPage, self).__init__()

    def PointUserUPS(self):
        '''点击用户画像'''
        self.PO.FindElement("css", "a[data-parent='#menu-500']", 0).Click()
        sleep(2)
        return True

    def PointUserLabel(self):
        '''点击用户标签'''
        self.PO.FindElement("css", "a[data-parent='#menu-500']", 1).Click()
        sleep(2)
        return True

    def PointLabelLibManage(self):
        '''点击标签库管理'''
        self.PO.FindElement("css", "a[data-parent='#menu-500']", 2).Click()
        sleep(2)
        return True

    def PointWorkplanManage(self):
        '''点击计划任务管理'''
        self.PO.FindElement("css", "a[data-parent='#menu-500']", 3).Click()
        sleep(2)
        return True

    def IntoUPSBeta(self):
        '''进入个人画像Beta'''
        self.PointUserUPS()
        selector = "a[href='/imp/a/ups/userDimension']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserUPS()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoFetchUserPage(self):
        '''进入提取用户'''
        self.PointUserLabel()
        selector = "a[href='/imp/a/ups/userTag']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserLabel()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoLabelManagePage(self):
        '''进入标签管理'''
        self.PointLabelLibManage()
        selector = "a[href='/imp/a/ups/upsLabel/labelType/lableTypeIndex']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointLabelLibManage()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoWorkplanManagePage(self):
        '''进入计划任务管理'''
        self.PointWorkplanManage()
        selector = "a[href='/imp/a/ups/scheduleJob']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointWorkplanManage()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

#####################################################################################################################

class UPSBeta(UpsSysPage):
    '''
    个人画像Beta
    '''
    def __init__(self):
        super(UPSBeta, self).__init__()
        self.IntoUPSBeta()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputUserInfo(self, userinfo):
        '''输入用户信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(userinfo)
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def GetUserInfo(self):
        '''获取用户昵称数据'''
        selector = "div[id='user_notes_msg'] > ul > li"
        EleOs = self.PO.FindElement("css", selector)
        return EleOs.text

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class FetchUserPage(UpsSysPage):
    '''
    提取用户
    '''
    def __init__(self):
        super(FetchUserPage, self).__init__()
        self.IntoFetchUserPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class LabelManagePage(UpsSysPage):
    '''
    标签管理
    '''
    def __init__(self):
        super(LabelManagePage, self).__init__()
        self.IntoLabelManagePage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True



class WorkplanManagePage(UpsSysPage):
    '''
    计划任务管理
    '''
    def __init__(self):
        super(WorkplanManagePage, self).__init__()
        self.IntoWorkplanManagePage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputWorkName(self, workname):
        '''输入任务名称'''
        selector = "job_name"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(workname)
        return True

    def InputWorkState(self, item=u'请选择'):
        '''选择任务状态'''
        seledict = {u'请选择':0, u'禁用':1, u'启用':2,  u'删除':3}

        #点击下拉
        self.PO.FindElement("class", "select2-choice").Click()

        #选择
        selector = "select[id='job_status'] > option"
        EleO = self.PO.FindElement("css", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True
