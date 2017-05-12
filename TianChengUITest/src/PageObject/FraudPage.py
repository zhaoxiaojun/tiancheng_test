#coding=utf8
#######################################################
#filename: FraudPage.py
#author: defias
#date: 2016-3
#function: Main Page
#######################################################
from MainPage import MainPage
from time import sleep

class FraudPage(MainPage):
    '''
    反欺诈平台
    '''
    def __init__(self):
        super(FraudPage, self).__init__()

    def PointFraudManage(self):
        '''点击反欺诈管理'''
        self.IntoFraudPage()
        self.PO.FindElement("css", "a[data-parent='#menu-100']", 0).Click()
        sleep(2)
        return True

    def PointBigDataControl(self):
        '''点击大数据风控'''
        self.IntoFraudPage()
        self.PO.FindElement("css", "a[data-parent='#menu-100']", 1).Click()
        sleep(2)
        return True

    def IntoFraudDetailPage(self):
        '''进入反欺诈调用明细'''
        self.PointFraudManage()
        selector = "a[href='/imp/a/afp/antiFraudDetailMode']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointFraudManage()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoSelfHelpPage(self):
        '''进入自助验证'''
        self.PointBigDataControl()
        selector = "a[href='/imp/a/afp/bigDataRiskCtrl/selfVerifyPage']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointBigDataControl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoIntelligentAlarmPage(self):
        '''进入预期智能预警'''
        self.PointBigDataControl()
        selector = "a[href='/imp/a/afp/bigDataRiskCtrl/overdueIntellEarlyWarningPage']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointBigDataControl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoChatLogsPage(self):
        '''进入聊天记录分析'''
        self.PointBigDataControl()
        selector = "a[href='/imp/a/afp/bigDataRiskCtrl/userChatLogAnalysisPage']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointBigDataControl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoPhoneAddressPage(self):
        '''进入手机通讯录分析'''
        self.PointBigDataControl()
        selector = "a[href='/imp/a/afp/bigDataRiskCtrl/mobileAddressList']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointBigDataControl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def IntoUserLocationPage(self):
        '''进入用户地理位置跟踪'''
        self.PointBigDataControl()
        selector = "a[href='/imp/a/afp/bigDataRiskCtrl/userLocationTrackPage']"
        EleO = self.PO.FindElement("css", selector)
        if not EleO.IsDisplayed():
            self.PointBigDataControl()
            EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True


class FraudDetailPage(FraudPage):
    '''
    反欺诈调用明细
    '''
    def __init__(self):
        super(FraudDetailPage, self).__init__()
        self.IntoFraudDetailPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        #framediy = {0:'default', 1:'jerichotabiframe'}  #页面frame定义
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

    def InputDate(self, item=u'当天'):
        '''选择日期'''
        seledict = {u'全部':"setDateImproved(5,'start_time','end_time','start_time_span','end_time_span','');",
        u'当天':"setDateImproved(0,'start_time','end_time','start_time_span','end_time_span','');",
        u'本周':"setDateImproved(1,'start_time','end_time','start_time_span','end_time_span','');",
        u'本月':"setDateImproved(3,'start_time','end_time','start_time_span','end_time_span','');",
        u'自选':"registerCalenOnclikImproved('start_time','end_time','start_time_span','end_time_span')"}

        #点击下拉
        self.PO.FindElement("id", "calanderDiv").Click()

        #选择
        # print 'item: ', item
        # print 'type item: ', type(item)

        # print 'decode item: ', item.decode('gbk')
        # print 'type decode item: ', type(item.decode('gbk'))

        # print 'seledict[item]: ', seledict[item]
        # print 'repr(seledict[item]): ', repr(seledict[item])

        selector = "a[onclick=" + repr(seledict[item]) + "]"
        EleO = self.PO.FindElement("css", selector)
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def InputResult(self, item=u'全部'):
        '''选择验证结果'''
        seledict = {u'全部':0, u'通过':1, u'拒绝':2, u'人工审核':3}

        #点击下拉
        self.PO.FindElement("class", "select2-choice").Click()

        #选择
        selector = "select2-result-label"
        EleO = self.PO.FindElement("class", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkExport(self):
        '''点击导出'''
        selector = "btnExport"
        self.PO.FindElement("id", selector).Click()
        return True

    def IntoBefor(self):
        '''点击上一页'''
        pass

    def IntoNext(self):
        '''点击下一页'''
        pass

    def GetData(self, *n):
        '''获取查询结果数据'''
        selector = "tbody[id='tbBody'] > tr[class='slidetr']"
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


class SelfHelpPage(FraudPage):
    '''
    自助验证
    '''
    def __init__(self):
        super(SelfHelpPage, self).__init__()
        self.IntoSelfHelpPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        #framediy = {0:'default', 1:'jerichotabiframe'}  #页面frame定义
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def IntoSingUser(self):
        '''点击单用户验证'''
        selector = "div['data_tab']>ul>li"
        EleO = self.PO.FindElement("css", selector, 0)
        EleO.Click()
        return True

    def IntoBatUser(self):
        '''点击批量户验证'''
        selector = "div['data_tab']>ul>li"
        EleO = self.PO.FindElement("css", selector, 1)
        EleO.Click()
        return True

    def InputUserName(self, username):
        '''输入用户名'''
        selector = "real_name"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(username)
        return True

    def InputPhoneNumber(self, phoneNumber):
        '''输入手机号'''
        selector = "mobile_phone"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(phoneNumber)
        return True

    def InputCardNumber(self, IDCard):
        '''输入身份证号'''
        selector = "id_no"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(IDCard)
        return True

    def CkYanzheng(self):
        '''点击验证按钮'''
        selector = "submit"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkZhima(self):
        '''勾选芝麻信用'''
        selector = "platform_no1"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkAijin(self):
        '''勾选爱金'''
        selector = "platform_no2"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkTongdun(self):
        '''勾选同盾'''
        selector = "platform_no3"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkQianhai(self):
        '''勾选前海征信'''
        selector = "platform_no4"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkPengyuan(self):
        '''勾选鹏元'''
        selector = "platform_no5"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkBairong(self):
        '''勾选百融'''
        selector = "platform_no6"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkLaolai(self):
        '''勾选法院老赖'''
        selector = "platform_no8"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkBlackName(self):
        '''勾选网贷黑名单'''
        selector = "platform_no9"
        self.PO.FindElement("id", selector).Click()
        return True

    def GetResultBorrowmoney(self):
        '''获取借款事件查询结果数据'''
        loc_type = "css"
        loc_value = "td[id='platform_no3_serivce_id5_result']>span"
        self.PO.PublicWaitEle(5, 0.5, loc_type, loc_value)
        return self.PO.FindElement(loc_type, loc_value).GetText()

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class IntelligentAlarmPage(FraudPage):
    '''
    预期智能预警
    '''
    def __init__(self):
        super(IntelligentAlarmPage, self).__init__()
        self.IntoIntelligentAlarmPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        #framediy = {0:'default', 1:'jerichotabiframe'}  #页面frame定义
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputBasicInfo(self, basicinfo):
        '''输入基本信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(basicinfo)
        return True

    def InputWarnType(self, item=u'全部'):
        '''选择预警类型'''
        seledict = {u'全部':0, u'疑似卸载软件':1, u'通讯录变更':2, u'地理位置变更':3}

        #点击下拉
        self.PO.FindElement("css", "div[id='s2id_warn_type']>a>span").Click()

        #选择
        selector = "select[id='warn_type']>option"
        EleO = self.PO.FindElement("css", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def InputStatus(self, item=u'全部'):
        '''选择处理状态'''
        seledict = {u'全部':0, u'未处理':1, u'处理':2}

        #点击下拉
        self.PO.FindElement("css", "div[id='s2id_status_early_warning']>a>span").Click()

        #选择
        selector = "select[id='status_early_warning']>option"
        EleO = self.PO.FindElement("css", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True


    def InputCalander(self, item=u'当天'):
        '''选择时间'''
        seledict = {u'当天':0, u'本周':1, u'上周':2, u'本月':3, u'上月':4}  #选择自定义还未实现

        #点击下拉
        self.PO.FindElement("css", "div[id='calanderDiv']>i").Click()

        #选择
        selector = "div[class='widget_menu']>ul>li"
        EleO = self.PO.FindElement("css", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def CkExport(self):
        '''点击导出'''
        selector = "btnExport"
        self.PO.FindElement("id", selector).Click()
        return True

    def QueryCheck(self):
        '''查询成功检查点'''
        loc_type = "css"
        loc_value = "tbody[id='tbBody']>tr>td>div"
        self.PO.PublicWaitEle(10, 0.5, loc_type, loc_value)
        EleO = self.PO.FindElement(loc_type, loc_value)
        return EleO.GetText()

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True



class ChatLogsPage(FraudPage):
    '''
    聊天记录分析
    '''
    def __init__(self):
        super(ChatLogsPage, self).__init__()
        self.IntoChatLogsPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputBasicInfo(self, basicinfo):
        '''输入基本信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(basicinfo)
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def InputCalander(self, item=u'当天'):
        '''选择时间'''
        seledict = {u'当天':0, u'本周':1, u'上周':2, u'本月':3, u'上月':4,  u'全部':5}  #选择自选还未实现

        #点击下拉
        self.PO.FindElement("css", "div[id='calanderDiv']>i").Click()

        #选择
        selector = "div[class='widget_menu']>ul>li"
        EleO = self.PO.FindElement("css", selector, seledict[item])
        EleO.Wait_Until_Visib(5, 0.5)
        EleO.Click()
        return True

    def QueryCheck(self):
        '''查询成功检查点'''
        loc_type = "css"
        loc_value = "ul[id='friend_list_ul']>li"
        self.PO.PublicWaitEle(5, 0.5, loc_type, loc_value)
        EleO = self.PO.FindElement(loc_type, loc_value)
        return EleO.GetText()

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True


class PhoneAddressPage(FraudPage):
    '''
    手机通讯录分析
    '''
    def __init__(self):
        super(PhoneAddressPage, self).__init__()
        self.IntoPhoneAddressPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputBasicInfo(self, basicinfo):
        '''输入基本信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(basicinfo)
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "submit123"
        self.PO.FindElement("id", selector).Click()
        return True

    def QueryCheck(self):
        '''查询成功检查点'''
        loc_type = "css"
        loc_value = "div[id='userInfoTable']>ul>li"
        self.PO.PublicWaitEle(10, 0.5, loc_type, loc_value)
        EleO = self.PO.FindElement(loc_type, loc_value)
        return EleO.GetText()

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True



class UserLocationPage(FraudPage):
    '''
    用户地理位置跟踪
    '''
    def __init__(self):
        super(UserLocationPage, self).__init__()
        self.IntoUserLocationPage()
        self.SwithFrame(1)

    def SwithFrame(self, framediy):
        '''Frame切换'''
        if framediy == 0:
            self.PO.SwithToFrame()
        elif framediy == 1:
            self.PO.SwithToFrame(loc_type='css', loc_value="iframe[id^='jerichotabiframe']")
        return True

    def InputBasicInfo(self, basicinfo):
        '''输入基本信息'''
        selector = "mobileOrIdCardNo"
        EleO = self.PO.FindElement("id", selector)
        EleO.Input(basicinfo)
        return True

    def CkQuery(self):
        '''点击查询'''
        selector = "btnSubmit"
        self.PO.FindElement("id", selector).Click()
        return True

    def QueryCheck(self):
        '''查询成功检查点'''
        loc_type = "css"
        loc_value = "ul[id='userBase_info']>li>p"
        self.PO.PublicWaitEle(10, 0.5, loc_type, loc_value)
        EleO = self.PO.FindElement(loc_type, loc_value)
        return EleO.GetText()

    def Close(self):
        '''关闭本TAB页'''
        self.SwithFrame(0)
        selector = ".tab_close>a"
        self.PO.FindElement("css", selector).Click()
        return True
