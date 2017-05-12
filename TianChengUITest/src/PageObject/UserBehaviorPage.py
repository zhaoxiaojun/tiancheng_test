#coding=utf8
#######################################################
#filename: UserBehaviorPage.py
#author: defias
#date: 2016-3
#function: User Behavior  Page
#######################################################
from MainPage import MainPage
from time import sleep

class UserBehaviorPage(MainPage):
    '''
    用户行为分析系统
    '''
    def __init__(self):
        super(UserBehaviorPage, self).__init__()

    def PointUserBaseAnl(self):
        '''点击用户基础分析'''
        self.IntoUserBehaviorPage()
        self.PO.FindElement("css", "a[data-parent='#menu-400']", 0).Click()
        sleep(2)
        return True

    def PointUserTerminalAnl(self):
        '''用户终端分析'''
        self.IntoUserBehaviorPage()
        self.PO.FindElement("css", "a[data-parent='#menu-400']", 1).Click()
        sleep(2)
        return True

    def PointUserActionAnl(self):
        '''点击用户行为分析'''
        self.IntoUserBehaviorPage()
        self.PO.FindElement("css", "a[data-parent='#menu-400']", 2).Click()
        sleep(2)
        return True

    def IntoUserOverviewPage(self):
        '''进入用户概况'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/basic/userProfiles']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserAreaPage(self):
        '''进入用户地区分布'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=region_area']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserJobPage(self):
        '''进入用户职业分布'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=occupation_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserIncomePage(self):
        '''进入用户收入分布'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=income_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserAssetsPage(self):
        '''进入用户资产分布'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=property_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserDebtPage(self):
        '''进入用户负债分布'''
        self.PointUserBaseAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=debt_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserBaseAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoTypePage(self):
        '''进入型号分布'''
        self.PointUserTerminalAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=model_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserTerminalAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoResolutionPage(self):
        '''进入分辨率分布'''
        self.PointUserTerminalAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=resolution_ratio']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserTerminalAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoOsVersionPage(self):
        '''进入操作系统版本分布'''
        self.PointUserTerminalAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=os_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserTerminalAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoNetworkOperatorsPage(self):
        '''进入网络及运营商分布'''
        self.PointUserTerminalAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=network_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserTerminalAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoTerminalValuePage(self):
        '''进入终端价值分布'''
        self.PointUserTerminalAnl()
        selector = "a[href='/imp/a/ubas/terminal?map.type=valuation_distribution']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserTerminalAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoBusinessTrackPage(self):
        '''进入用户业务轨迹分析'''
        self.PointUserActionAnl()
        selector = "a[href='/imp/a/ubas/business/track/statistics/page']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserActionAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoOperatorTrackPage(self):
        '''进入用户操作轨迹分析'''
        self.PointUserActionAnl()
        selector = "a[href='/imp/a/ubas/business/opt/track/page']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointUserActionAnl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

#####################################################################################################################

class UserOverviewPage(UserBehaviorPage):
    '''
    用户概况
    '''
    def __init__(self):
        super(UserOverviewPage, self).__init__()
        self.IntoUserOverviewPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetUserTotal(self, userinfo):
        '''获取用户总数'''
        selector = "ul[id='ul_verity'] > li"
        EleO = self.PO.FindElement("css", selector, 0)
        return int(EleO.GetText())

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class UserUserAreaPage(UserBehaviorPage):
    '''
    用户地区分布
    '''
    def __init__(self):
        super(UserUserAreaPage, self).__init__()
        self.IntoUserAreaPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class UserUserJobPage(UserBehaviorPage):
    '''
    用户职业分布
    '''
    def __init__(self):
        super(UserUserJobPage, self).__init__()
        self.IntoUserJobPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class UserIncomePage(UserBehaviorPage):
    '''
    用户收入分布
    '''
    def __init__(self):
        super(UserUserJobPage, self).__init__()
        self.IntoUserIncomePage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class UserAssetsPage(UserBehaviorPage):
    '''
    用户资产分布
    '''
    def __init__(self):
        super(UserAssetsPage, self).__init__()
        self.IntoUserAssetsPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class UserDebtPage(UserBehaviorPage):
    '''
    用户负债分布
    '''
    def __init__(self):
        super(UserDebtPage, self).__init__()
        self.IntoUserDebtPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True



#####################################################################################################################

class TypePage(UserBehaviorPage):
    '''
    型号分布
    '''
    def __init__(self):
        super(TypePage, self).__init__()
        self.IntoTypePage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbBody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class ResolutionPage(UserBehaviorPage):
    '''
    分辨率分布
    '''
    def __init__(self):
        super(ResolutionPage, self).__init__()
        self.IntoResolutionPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbBody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class OsVersionPage(UserBehaviorPage):
    '''
    操作系统版本分布
    '''
    def __init__(self):
        super(OsVersionPage, self).__init__()
        self.IntoOsVersionPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbBody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class NetworkOperatorsPage(UserBehaviorPage):
    '''
    网络及运营商分布
    '''
    def __init__(self):
        super(NetworkOperatorsPage, self).__init__()
        self.IntoNetworkOperatorsPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbBody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True

class TerminalValuePage(UserBehaviorPage):
    '''
    终端价值分布
    '''
    def __init__(self):
        super(TerminalValuePage, self).__init__()
        self.IntoTerminalValuePage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def GetDataDail(self, *n):
        '''获取数据明细'''
        selector = "tbody[id='tbBody'] > tr"
        EleOs = self.PO.FindElements("css", selector)
        if n:
            EleOs = EleOs[:n[0]]
        datas = [x.GetText().split() for x in EleOs]
        return len(datas)

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class BusinessTrackPage(UserBehaviorPage):
    '''
    用户业务轨迹分析
    '''
    def __init__(self):
        super(BusinessTrackPage, self).__init__()
        self.IntoBusinessTrackPage()
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
        selector = "div[id='userInfoTable'] > div > ul > li"
        EleOs = self.PO.FindElement("css", selector)
        return EleOs.text

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class OperatorTrackPage(UserBehaviorPage):
    '''
    用户操作轨迹分析
    '''
    def __init__(self):
        super(OperatorTrackPage, self).__init__()
        self.IntoOperatorTrackPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputUserInfo(self, userinfo):
        '''输入基本信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(userinfo)
        return True

    def InputDate(self, item=u'当天'):
        '''选择日期'''
        seledict = {u'全部':"setDateImproved(6,'start_time','end_time','start_time_span','end_time_span','');",
        u'当天':"setDateImproved(0,'start_time','end_time','start_time_span','end_time_span','');",
        u'本周':"setDateImproved(1,'start_time','end_time','start_time_span','end_time_span','');",
        u'上周':"setDateImproved(2,'start_time','end_time','start_time_span','end_time_span','');",
        u'本月':"setDateImproved(3,'start_time','end_time','start_time_span','end_time_span','');",
        u'上月':"setDateImproved(4,'start_time','end_time','start_time_span','end_time_span','');",
        u'自定义':"registerCalenOnclikImproved('start_date','end_date','start_date_span','end_date_span')"}

        #点击下拉
        self.PO.FindElement("id", "calanderDiv").Click()

        #选择
        selector = "a[onclick=" + repr(seledict[item]) + "]"
        EleO = self.PO.FindElement("css", selector)
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "submit"
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
