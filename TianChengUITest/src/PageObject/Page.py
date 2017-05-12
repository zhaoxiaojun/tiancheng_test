#coding=utf8
#######################################################
#filename: Page.py
#author: defias
#date: 2016-3
#function: Base Page Operation
#######################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#定位方式
Locate = {"id":By.ID, "class":By.CLASS_NAME, "css":By.CSS_SELECTOR, "link":By.LINK_TEXT, "name":By.NAME,"partlink":By.PARTIAL_LINK_TEXT,
"tag":By.TAG_NAME, "xpath":By.XPATH}

def ChangeEleO(func):
    '''
    装饰器：将元素包装成Ele对象
    '''
    def wrapper(self, loc_type, loc_value, *locn):
        ele = func(self, loc_type, loc_value, *locn)
        if type(ele) is list:
            Res = [Ele(x) for x in ele]
        else:
            Res = Ele(ele)
        return Res
    return wrapper


class Page(object):
    '''
    基本Driver类，用于所有页面继承
    '''
    def __new__(cls, *a, **k):   #单例模式
        if not hasattr(cls, '_inst'):
            cls._inst = super(Page, cls).__new__(cls, *a, **k)
        return cls._inst

    def OpenUrl(self, browser, url):
        '''打开URL地址'''
        if not hasattr(self, 'driverO'):
            if browser == 'chrome':
                self.driverO = webdriver.Chrome()  #驱动
            elif browser == 'firefox':
                self.driverO = webdriver.Firefox()
            else:
                return False
            self.driverO.implicitly_wait(10)     #隐式等待
        self.driverO.get(url)
        return True

    @ChangeEleO
    def FindElement(self, loc_type, loc_value, *locn):
        '''元素定位'''
        if not locn:
            ele = self.driverO.find_element(Locate[loc_type], loc_value)
        else:
            eles = self.driverO.find_elements(Locate[loc_type], loc_value)
            ele = eles[locn[0]]
        return ele

    @ChangeEleO
    def FindElements(self, loc_type, loc_value):
        '''元素组定位'''
        eles = self.driverO.find_elements(Locate[loc_type], loc_value)
        return eles

    def SwithToFrame(self, **frameParam):
        '''切换Frame'''
        #{'frameid':'xxx'} {'framename':'xxx'} {'loc_type': 'css', 'loc_value':'xxxx', 'locn': 0}
        if frameParam:
            if 'frameid' in frameParam:
                frameid = frameParam['frameid']
                self.driverO.switch_to_frame(frameid)
            elif 'framename' in frameParam:
                framename = frameParam['framename']
                self.driverO.switch_to_frame(framename)
            else:
                loc_type = frameParam['loc_type']
                loc_value = frameParam['loc_value']
                if 'locn' in frameParam:
                    locn = frameParam['locn']
                    eleO = self.driverO.find_elements(Locate[loc_type], loc_value)[locn]
                else:
                    eleO = self.driverO.find_element(Locate[loc_type], loc_value)
                self.driverO.switch_to_frame(eleO)
        else:
            self.driverO.switch_to_default_content()     #切换到默认内容，跳出原来的Frame
        return True

    def isPresent(self, loc_type, loc_value):
        '''判断某个待定位的元素是否存在'''
        try:
            self.driverO.find_element(Locate[loc_type], loc_value)
            return True
        except NoSuchElementException:
            return False

    def HideWait(self, t):
        '''隐式等待'''
        self.driverO.implicitly_wait(t)

    def PublicWaitEle(self, t, lt, loc_type, loc_value):
        '''等待某个待定位的元素直到存在 t: 等待总时间  lt: 检查时间间隔 '''
        WebDriverWait(self.driverO, t, lt).until(lambda x: x.find_element(Locate[loc_type], loc_value))

    def RunJs(self):
        '''执行js脚本'''
        self.driverO.execute_script()
        return True

    def CloseBrowser(self):
        '''关闭浏览器'''
        self.driverO.close()
        #self.driverO.quit()
        return True


class Ele(object):
    '''
    元素对象操作
    '''
    def __init__(self, elementO):
        self.eO = elementO
        self.PO = Page()

    def FindSubElement(self, loc_type, loc_value, *locn):
        '''元素定位'''
        if not locn:
            ele = self.eO.find_element(Locate[loc_type], loc_value)
        else:
            eles = self.eO.find_elements(Locate[loc_type], loc_value)
            ele = eles[locn[0]]
        return ele

    def Input(self, value):
        '''输入'''
        self.eO.send_keys(value)
        return True

    def Click(self):
        '''单击'''
        self.eO.click()
        return True

    def GetText(self):
        '''获取文本'''
        return self.eO.text

    def IsDisplayed(self):
        '''是否显示'''
        return self.eO.is_displayed()


    def Wait_Until_Visib(self, t, tval):
        '''显示等待本元素可见'''
        WebDriverWait(self.PO.driverO, t, tval).until(EC.visibility_of(self.eO))
