#coding=utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from IndexPage import IndexPage
from MainPage import MainPage
from FraudPage import FraudPage, FraudDetailPage, SelfHelpPage
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'http://192.168.18.77:8080/imp/a/login'

def isPresent(driverO, loc_value):
    try:
        driverO.find_element(By.CSS_SELECTOR, loc_value)
        return True
    except NoSuchElementException:
        return False

def HideWait(driverO, t):
    driverO.implicitly_wait(t)


def PublicWaitEle(driverO, t, lt, loc_value):
    WebDriverWait(driverO, t, lt).until(lambda x: x.find_element(By.CSS_SELECTOR, loc_value))


def Testing():
    driverO = webdriver.Chrome()
    driverO.get(url)
    #driverO.find_element(By.ID, "username").send_keys('root')
    driverO.find_element(eval("By.ID"), "username").send_keys('root')
    driverO.find_element(By.ID, "password").send_keys('root123')
    driverO.find_element(By.CLASS_NAME, 'login_btn').click()

    driverO.find_element(By.CSS_SELECTOR, 'a[data-id="100"]').click()
    sleep(3)
    driverO.find_element(By.CSS_SELECTOR, ".tab_close>a").click()

    driverO.find_elements(By.CSS_SELECTOR, "a[data-parent='#menu-100']")[1].click()
    sleep(3)
    driverO.find_element(By.CSS_SELECTOR, 'a[href="/imp/a/afp/bigDataRiskCtrl/userChatLogAnalysisPage"]').click()

    #sleep(3)
    swichele = driverO.find_element(By.CSS_SELECTOR, "iframe[id^='jerichotabiframe']")
    driverO.switch_to_frame(swichele)
    print "======",
    sleep(3)

    #driverO.find_element(By.ID, "mobileOrIdCardNo").send_keys("test123")
    #sleep(1)

    driverO.find_element(By.ID, "mobileOrIdCardNo").send_keys("15112526410")



    driverO.find_element(By.ID, "btnSubmit").click()

    loc_value = "ul[id='friend_list_ul']>li"
    if not isPresent(driverO, loc_value):
        #locw_value = "ul[id='friend_list_ul']>li"
        HideWait(driverO, 5)
        #PublicWaitEle(driverO, 5, 0.5, locw_value)
        #WebDriverWait(driverO, 5, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, locw_value))
    print driverO.find_element(By.CSS_SELECTOR, "ul[id='friend_list_ul']>li").text



    # driverO.find_element(By.ID, "calanderDiv").click()
    # sleep(1)

    # selector = "a[onclick=" + repr("setDateImproved(5,'start_time','end_time','start_time_span','end_time_span','');") + "]"
    # driverO.find_element(By.CSS_SELECTOR, selector).click()


    # driverO.find_element(By.CLASS_NAME, "select2-choice").click()
    # sleep(3)

    # driverO.find_elements(By.CLASS_NAME, "select2-result-label")[0].click()
    # sleep(1)

    # driverO.find_element(By.ID, "btnSubmit").click()
    # sleep(1)
    # print '==================='

    # #获取数据
    # data = driverO.find_elements(By.CSS_SELECTOR, "tbody[id='tbBody'] > tr[class='slidetr']")
    # print 'data of len: ', len(data)
    # print 'text:\n'
    # print 'type: ', type(data[0].text)
    # print data[0].text

    # datalist = data[0].text.split()
    # print 'type: ', type(datalist)
    # print datalist

    # print datalist[1].encode('gbk')







    #driverO.switch_to_default_content()
    #sleep(1)

    #driverO.find_elements(By.CSS_SELECTOR, ".tab_close>a")[0].click()
    #sleep(1)
    #print '==================='
    #driverO.find_elements(By.CSS_SELECTOR, "a[data-parent='#menu-100']").pop(1).click()
    #driverO.find_elements_by_css_selector("a[data-parent='#menu-100']")[1].click()
    #sleep(1)


    # try:
    #     WE = driverO.find_element(By.CSS_SELECTOR, 'a[href="/imp/a/afp/bigDataRiskCtrl/selfVerifyPage"]')
    #     print WE.__class__
    #     print 111

    #     WebDriverWait(driverO,5,0.5).until(EC.visibility_of(WE))

    #     if WE.is_displayed():
    #         print WE.is_displayed()
    #     else:
    #         print WE.is_displayed()

    #     WE.click()
    #     print 222
    # except NoSuchElementException as n:
    #     print 444
    #     print n
    # except ElementNotVisibleException as v:
    #     print 333
    #     print v
    # except TimeoutException as tout:
    #     print 666
    #     print tout
    # except Exception as e:
    #     print 555
    #     print e

def TestPO():
    IndexPageO = IndexPage()

    IndexPageO.Open(url)

    IndexPageO.InputUser('root')

    IndexPageO.InputPasswd('root123')
    IndexPageO.CkJZWCheckBox()
    IndexPageO.CkLoginButton()

    #MainPageO = MainPage()
    #MainPageO.IntoFraudPage()

    #FraudPageO = FraudPage()
    #FraudPageO.IntoFraudDetailPage()

    FraudDetailPageO = FraudDetailPage()
    #FraudDetailPageO.SwithFrame(1)
    print '1---' + str(FraudDetailPageO.InputUserInfo('15112526410'))
    print '2---' + str(FraudDetailPageO.InputDate(u'全部'))
    print '3---' + str(FraudDetailPageO.InputResult(u'全部'))
    print '4---'+ str(FraudDetailPageO.CkQuery())
    print '5---:', FraudDetailPageO.GetData(1)
    sleep(3)
    FraudDetailPageO.Close()
    sleep(5)

    #SelfHelpPageO = SelfHelpPage()
    #SelfHelpPageO.InputUserName('www')
    #SelfHelpPageO.CkYanzheng()

    IndexPageO.Close()

    #IndexPageO = IndexPage()
    #print IndexPageO.PO
    IndexPageO.Open(url)
    #print IndexPageO.PO.driverO

    #FraudDetailPageO.SwithFrame(0)

    #print '5---'+ str(FraudDetailPageO.Close())

    #FraudPageO.IntoSelfHelpPage()


    # sleep(5)
    # print '==================='
    # #FraudDetailPageO.Logout()


if __name__ == '__main__':
    Testing()
    #TestPO()
    sleep(5)
