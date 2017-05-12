#coding=utf8
#######################################################
#filename: TestCaseGenerator.py
#author: defias
#date: 2016-4
#function: TestCase Generator
#######################################################
import time, os
import inspect
import codecs
from Public import Function
from PageObject import *
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestCaseTemplate_mixin(object):
    """
    Define a TestCase template for testcase*.py

    testcase*.py
    +------------------------+
    |   header               |
    |                        |
    |   import module        |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |                        |
    |   class defined        |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   fixed method         |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   testcase  method     |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    +------------------------+
    """

    header = r"""#coding=utf8
#######################################################
#filename: %(filen)s
#author: TestCaseGenerator
#date: %(now)s
#function: unittest test case
#######################################################
"""

    importModule = r"""import unittest,time,os,sys
sys.path.append(os.environ['TCWT_HOME'] + '\\src\\')
from Login import Login
from PageObject import *


"""

    classDefined = r"""class %(classn)s(unittest.TestCase):"""

    fixedMethod = r"""
    @classmethod
    def setUpClass(cls):
        url = '%(u)s'
        browser = '%(br)s'
        cls.LoginO = Login()
        cls.LoginO.open(browser, url)  #open web page

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.LoginO.login()  #login

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.assertEqual(self.verificationErrors, [])
        self.LoginO.logout()  #logout

    @classmethod
    def tearDownClass(cls):
        cls.LoginO.close()  #close web page
"""



class TestMethodGenerator(object):
    '''生成测试方法'''

    def _writeTcMethodDefined(self, methodname):
        '''方法定义'''
        methodDefined = r"""
    def %(method)s(self):
""" % dict(method = methodname)
        self.fp.writelines(methodDefined)

    def _writeTcComment(self, methodcomment):
        '''方法注释'''
        self.fp.writelines("""        u'''""")
        self.fp.writelines(methodcomment)
        self.fp.writelines("""'''
""")

    def _wiriteTcObjectDefined(self, pageomodule, pageo):
        '''操作页面对象定义'''
        objectDefined = r"""        po = %(pmodule)s.%(po)s()
""" % dict(pmodule = pageomodule, po = pageo)
        self.fp.writelines(objectDefined)

    def _writeTcOperationSt(self, operation, *values):
        '''操作语句'''
        if values:
            value = values[0]
            operationSt = r"""        po.%(oper)s(u'%(ve)s')
""" % dict(oper = operation, ve = value)
        else:
            operationSt = r"""        po.%(oper)s()
""" % dict(oper = operation)

        self.fp.writelines(operationSt)

    def _writeTcAssert(self, assertmethod, checkmethod, exp):
        '''断言语句'''
        if type(exp) is int:
            assertSt = r"""        self.%(amethod)s(po.%(cmethod)s(), %(ex)s)
""" % dict(amethod = assertmethod, cmethod = checkmethod, ex = exp)
        elif type(exp) is str:
            assertSt = r"""        self.%(amethod)s(po.%(cmethod)s(), "%(ex)s")
""" % dict(amethod = assertmethod, cmethod = checkmethod, ex = exp)
        self.fp.writelines(assertSt)



class TestCaseGenerator(TestCaseTemplate_mixin, TestMethodGenerator):
    """测试用例生成器"""
    def __init__(self, testcaseXml):  #testcaseXml：TestFraud.xml
        self.testcaseXml = testcaseXml
        self.testcasePy = 'Auto' + self.testcaseXml.split('.')[-2] + '.py'
        self.filePath = Function.memdata.getvalue() + "\\src\\TestCaseLib\\" + self.testcasePy
        self.fp = codecs.open(self.filePath,"w","utf-8")
        xmlPath = Function.memdata.getvalue() + "\\src\\" + self.testcaseXml
        self.tree = ET.parse(xmlPath)
        self.root = self.tree.getroot()

    def writeEnd(self):
        '''结束'''
        self.fp.flush()
        self.fp.close()

    def writeHeader(self):
        '''头语句'''
        nowDate = time.strftime("%Y-%m-%d %H:%M:%S")
        Header = self.header % dict(filen = self.testcasePy, now = nowDate)
        self.fp.writelines(Header)

    def wiriteImportModule(self):
        '''模块导入语句'''
        ImportModule = self.importModule
        self.fp.writelines(ImportModule)

    def writeClassDefined(self):
        '''测试类定义语句'''
        classname = self.testcaseXml.split('.')[-2]
        ClassDefined = self.classDefined % dict(classn = classname)
        self.fp.writelines(ClassDefined)

    def writeFixedMethod(self):
        '''固定方法语句'''
        browser = self.root.find('setting').findtext('browser')
        app_url = self.root.find('setting').findtext('app_url')

        FixedMethod = self.fixedMethod % dict(u = app_url, br = browser)
        self.fp.writelines(FixedMethod)

    def writeTestcaseMethod(self):
        '''测试方法（用例）'''
        testcaseEles = self.root.findall('testcase')
        for testcaseEle in testcaseEles:
            testcaseid = testcaseEle.attrib['id']
            methodcomment = testcaseEle.attrib['name']
            methodname = 'test_' + self.testcaseXml.split('.')[-2][4:] + '_' + testcaseid
            self._writeTcMethodDefined(methodname)
            self._writeTcComment(methodcomment)

            pageo = testcaseEle.findtext('pageo')
            pageomodule = self._getPageomd(pageo)
            self._wiriteTcObjectDefined(pageomodule, pageo) #对象定义

            stepsEle = testcaseEle.find('steps').findall('step')  #测试操作
            for stepEle in stepsEle:
                operation = stepEle.findtext('operation')
                value = stepEle.findtext('value')
                if value:
                    self._writeTcOperationSt(operation, value)
                else:
                    self._writeTcOperationSt(operation)

            #断言语句
            assertEle = testcaseEle.find('assert')
            assertmethod = assertEle.findtext('assertmethod')
            checkmethod = assertEle.findtext('checkmethod')

            expEle = assertEle.find('exp')
            expvalue = expEle.text
            exptype = expEle.attrib['type']
            if exptype == 'int':
                expvalue = int(expvalue)
            elif exptype == 'str':
                if type(expvalue) is not str:
                    expvalue = ''

            self._writeTcAssert(assertmethod, checkmethod, expvalue)

    def _getPageomd(self, pageo):
        '''根据页面对象pageo获取所在模块'''
        result = None
        #PageObject库中的所有模块
        pageoDir = Function.memdata.getvalue() + '\\src\\PageObject\\'
        testmds = [x[:-3] for x in os.listdir(pageoDir) if os.path.splitext(x)[1]=='.py' and os.path.splitext(x)[0][-4:]=='Page' and os.path.splitext(x)[0][:4]!='Page']
        for testmd in testmds:
            clsmembers = inspect.getmembers(eval(testmd), inspect.isclass)  #获取模块中的所有类
            for clsmember in clsmembers:
                if pageo == clsmember[0]:
                    result = testmd
                    break
            break
        if result is None:
            raise
        return result


def DriverGenerator(testcaseDir):
    '''用例生成器驱动'''
    xmlfiles = [x for x in os.listdir(testcaseDir) if os.path.splitext(x)[-1]=='.xml']
    for xmlfile in xmlfiles:
        TestCaseGeneratorO = TestCaseGenerator(xmlfile)
        TestCaseGeneratorO.writeHeader()
        TestCaseGeneratorO.wiriteImportModule()
        TestCaseGeneratorO.writeClassDefined()
        TestCaseGeneratorO.writeFixedMethod()
        TestCaseGeneratorO.writeTestcaseMethod()
        TestCaseGeneratorO.writeEnd()

def Run():
    '''启动用例生成器'''
    testcaseDir = Function.memdata.getvalue() + '\\src\\'
    DriverGenerator(testcaseDir)


