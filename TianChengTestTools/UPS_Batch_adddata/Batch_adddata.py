#coding=utf8
####################################################################
#filename:Batch_adddata.py
#author:defias
#date:2015-10
#function: 批量数据生成
#参数说明：functioncode--功能码   nums--批量插入数据的条数
####################################################################
'''
用户画像：
-------------------------------------------------------------------------------------------------------------------
表中文名                       对应表名                     对应接口
用户基本信息表                 userbasicinfo
用户工作信息表                 workinfo
用户车产信息表                 usercarpropertyinfo
用户房产信息表                 userhousepropertyinfo
用户登录事件表(按日期分表)     loginevent                   PostUserLogin   注册-用户登录
担保事件表(按日期分表)         PostGuaranteeEvent           PostGuarantee    立即担保显示页面
借款事件表(按日期分表)         PostPublishBorrowMoneyEvent  PostPublishBorrowMoney  借款--我要借款
投资事件表(按日期分表)         PostInvestmentEvent          PostInvestment  立即投资显示页面事件
充值事件表(按日期分表)         PostLianLianRechargeEvent    payment/PostLianLianRechargecharge    连连充值
逾期信息表(按时间分表)         OverdueInfo
-------------------------------------------------------------------------------------------------------------------
'''
import MySQLdb
import random
import time
import uuid
import sys
import base64
from Custom_Request import Http_Custom_Request
reload(sys)
sys.setdefaultencoding("utf8")   #设置默认字符串编码为utf8，否则为ascii

def Add_oneuserface_testdata():
    #初始化接口请求
    crd = Http_Custom_Request('http://192.168.18.77:8080/uap/api/ubas')
    headers = {"APPID":10, "TOKEN":"abcdefghijk"}
    crd.set_header(headers)

    #当前时间
    now = time.localtime(time.time())
    nowstr =  time.strftime("%Y-%m-%d %H:%M:%S", now)
    print 'nowstr',nowstr

    #随机生成userId
    userId = "testing-" + str(uuid.uuid1())
    print 'userId',userId

    #注册-用户登录
    data = '{"FunctionCode":"1003000003","MsgBody":{"result":{"message":"登录成功","result":"1","totalCount":0},"module":"UserApi","operateTime":"' + nowstr + '","param":{"RegistrationId":"010b8c44773","IP":"","userName":"13500000023","Latitude":"40.049246","Longitude":"116.296447","password":"**********","DevType":"Android","fromType":"3"},"tableName":"","userId":"' + userId + '","method":"PostUserLogin","ip":"192.168.1.88"},"CurrentTime":"' + nowstr + '"}}'
    try:
        response = crd.post(data)
        if eval(response.content)['Status'] != '0':
            return -1
    except:
        return -1
    print '注册-用户登录接口请求完成'

    #立即担保显示页面
    data = '{"FunctionCode":"1003000031","MsgBody":{"result":{"message":"操作成功","result":"1","totalCount":0},"module":"GuaranteeApi","operateTime":"' + nowstr + '","param":{"UserId":"' + userId + '","ProjectId":"102949"},"tableName":"","userId":"' + userId + '","method":"PostGuarantee","ip":"120.234.2.106"},"CurrentTime":"' + nowstr + '"}}'
    try:
        response = crd.post(data)
        if eval(response.content)['Status'] != '0':
            return -1
    except:
        return -1
    print '立即担保显示页面'

    #借款--我要借款
    data = '{"FunctionCode":"1003000023","MsgBody":{"result":{"message":"操作成功","result":"1","totalCount":0},"module":"LoanApi","operateTime":"' + nowstr + '","param":{"BorrowerRate":"8","AmountUsedDesc":"测试的数据","RepaymentTypeId":"1","Area":"南城区","Latitude":"23.5","Longitude":"123.4","UserId":"' + userId + '","Deadline":"2","BorrowerAmount":"6000","GuaranteeRate":"4","Title":"测试借款数据111","City":"东莞市"},"tableName":"","userId":"' + userId + '","method":"PostPublishBorrowMoney","ip":"0:0:0:0:0:0:0:1"},"CurrentTime":"' + nowstr + '"}}'
    try:
        response = crd.post(data)
        if eval(response.content)['Status'] != '0':
            return -1
    except:
        return -1
    print '借款--我要借款请求完成'

    #立即投资显示页面事件
    data = '{"FunctionCode":"1003000027","MsgBody":{"result":{"message":"操作成功","result":"1","totalCount":0},"module":"InvestigationApi","operateTime":"' + nowstr + '","param":{"UserId":"' + userId + '","ProjectId":"102931"},"tableName":"","userId":"' + userId + '","method":"PostInvestment","ip":"163.177.171.38"},"CurrentTime":"' + nowstr + '"}}'
    try:
        response = crd.post(data)
        if eval(response.content)['Status'] != '0':
            return -1
    except:
        return -1
    print '立即投资显示页面事件'

    #连连充值
    data = '{"FunctionCode":"1003000043","MsgBody":{"result":{"message":"操作成功","result":"1","totalCount":0},"module":"BankCardApi","operateTime":"' + nowstr + '","param":{"TradeDate":"1439518040","SignType":"MD5","UserId":"' + userId + '","BankAreaName":"河北省保定市阜平县","BankName":"招商银行","DeviceType":"1","MoneyOrder":"500000.00","BankArea":"130624","IsNewCard":false,"BankSubBranch":"","InputCharset":"utf-8","BankCity":"130600","UserMobile":"18888888802","PayPassword":"**********","Sign":"cd88f253c876c0ae40015f1b4ffadaad","BankCode":"03080000","BankAccount":"6225887865411033","BankProvince":"130000"},"tableName":"","userId":"' + '1ccf1106-9d6b-4420-a60b-185ea887655b' + '","method":"payment/PostLianLianRecharge","ip":"218.17.157.50"},"CurrentTime":"' + nowstr + '"}}'
    try:
        response = crd.post(data)
        if eval(response.content)['Status'] != '0':
            return -1
    except:
        return -1
    print '连连充值请求完成'

    #初始化数据库
    conn = MySQLdb.connect(host='192.168.18.69',user='root',passwd='niiwooroot',port=3306,charset='utf8')  #连接数据库
    conn.select_db('ubas_tianchengtest')  #选择数据库
    cur = conn.cursor()



    #用户基本信息表
    cur.execute("INSERT INTO userbasicinfo(UserId, LoginFromOthers, Istuandai, RegisterTime, MaritalStatus, ChildrenStatus, LivingProvince, LivingCity, LivingArea, LivingAddress, CardAddress, GraduateSchool, UserIDCard) VALUES(%s, %s, %s, %s, %s)", ())





    return 0


def Batch_adddata_pctest(nums):
    pass

#loginevent


if __name__ == '__main__':
    Add_oneuserface_testdata()
