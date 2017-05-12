#coding=utf8
####################################################################
#filename:Batch_adddata_pctest.py
#author:defias
#date:2015-8
#function: 生成反欺诈接口数据库批量数据
#参数说明：functioncode--功能码   nums--批量插入数据的条数
####################################################################
import MySQLdb
import random
import time
import uuid
import sys
import base64

reload(sys)
sys.setdefaultencoding("utf8")

def Batch_adddata_pctest(functioncode,nums):
    conn = MySQLdb.connect(host='192.168.18.66',user='niiwoowrite',passwd='4lVX7SO7LmDJ',port=3306,charset='utf8')  #连接业务数据库
    conn.select_db('niiwoo_test150919')  #选择业务数据库
    cur = conn.cursor()

    #从业务数据库中得到100000条用户数据
    count = cur.execute("SELECT u.id AS userId, p.id AS projectId, u.identityCard, u.credTypeId, u.realName, u.mobileNo FROM tnw_userBasicInfo u, tnw_project p  WHERE u.id = p.userId AND u.identityCard IS NOT NULL AND u.realName IS NOT NULL AND u.mobileNo IS NOT NULL AND p.id IS NOT NULL LIMIT 100000")
    print 'count',count
    userdata_rows = cur.fetchmany(nums)
    print 'userdata_rows',userdata_rows

    conn.commit()
    #关闭数据库连接
    cur.close()
    conn.close()

    if nums > count:
        print 'nums is too big!'
        return -1
    conn = MySQLdb.connect(host='192.168.18.69',user='root',passwd='niiwooroot',port=3306,charset='utf8')  #连接测试数据库
    conn.select_db('ytest_pctest_fraud')  #选择测试数据库
    cur = conn.cursor()
    #借款人获取额度
    if functioncode == 100122:
        enFraudCheckModelType = '3'   #enFraudCheckModelType
        enFraudCheckHandleStatus = '1'  #enFraudCheckHandleStatus
        ReqTime = '0'   #ReqTime

        n = 0
        while n < nums:   #循环向pct_afp_tianchengtest.fraudcheckmodelreq中插入数据
            #UniqueID
            UniqueID = str(uuid.uuid1())

            #ReqJson
            ReqJson_parttou = '{"FunctionCode":"100122","CurrentTime":"20150723203212000000","MsgBody":{"bank_cart":"12345","reasonno":"04","blackBox":"123","ip":"192.168.1.122","account_login":"test123",'
            ReqJson_partend = '}}'
            ReqJson_part ='"UniqueID":"' + UniqueID + '","user_id":"' + str(userdata_rows[n][0]) + '","identity_card":"' + str(userdata_rows[n][2]) + '","idtype":"' + str(userdata_rows[n][3]) + '","mobile_phone":"' + str(userdata_rows[n][5]) + '","name":"' + str(userdata_rows[n][4]) +'"'
            ReqJson = ReqJson_parttou + ReqJson_part + ReqJson_partend
            print 'ReqJson: ',ReqJson
            ReqJson = base64.b64encode(ReqJson)
            print 'ReqJsonbase64:',ReqJson

            #插入数据库
            cur.execute("INSERT INTO fraudcheckmodelreq(UniqueID, ReqJson, enFraudCheckModelType, ReqTime, enFraudCheckHandleStatus) VALUES(%s, %s, %s, %s, %s)", (UniqueID.encode('utf-8'),ReqJson.encode('utf-8'),enFraudCheckModelType.encode('utf-8'),ReqTime.encode('utf-8'),enFraudCheckHandleStatus.encode('utf-8')))

            #自增循环变量
            n = n + 1
    #担保人申请资格
    elif functioncode == 100126:
        enFraudCheckModelType = '2'   #enFraudCheckModelType
        enFraudCheckHandleStatus = '1'  #enFraudCheckHandleStatus
        ReqTime = '0'   #ReqTime
        n = 0
        while n < nums:  #循环向pct_afp_tianchengtest.fraudcheckmodelreq中插入数据
            #UniqueID
            UniqueID = str(uuid.uuid1())

            #ReqJson
            ReqJson_parttou = '{"FunctionCode":"100126","CurrentTime":"20150723203212000000","MsgBody":{"bank_cart":"12345","reasonno":"04","blackBox":"abc","ip":"192.168.1.122","account_login":"test123","currency":"23232","applyDate":"2015-08-01","creditAddress":"北京","is_student":0,"role":1,"degree":"1","isVerify":1,'
            ReqJson_partend = '}}'
            ReqJson_part = '"UniqueID":"' + UniqueID + '","user_id":"' + str(userdata_rows[n][0]) + '","identity_card":"' + str(userdata_rows[n][2]) + '","idtype":"' + str(userdata_rows[n][3]) + '","mobile_phone":"' + str(userdata_rows[n][5]) + '","name":"' + str(userdata_rows[n][4]) +'"'
            ReqJson = ReqJson_parttou + ReqJson_part + ReqJson_partend
            print 'ReqJson:',ReqJson
            ReqJson = base64.b64encode(ReqJson)
            print 'ReqJsonbase64:',ReqJson
            #插入数据库
            cur.execute("INSERT INTO fraudcheckmodelreq(UniqueID, ReqJson, enFraudCheckModelType, ReqTime, enFraudCheckHandleStatus) VALUES(%s, %s, %s, %s, %s)", (UniqueID,ReqJson,enFraudCheckModelType,ReqTime,enFraudCheckHandleStatus))
            #自增循环变量
            n = n + 1
    #借款人发布借款
    elif functioncode == 100124:
        enFraudCheckModelType = '1'   #enFraudCheckModelType
        enFraudCheckHandleStatus = '1'  #enFraudCheckHandleStatus
        ReqTime = '0'   #ReqTime
        n = 0
        while n < nums:  #循环向pct_afp_tianchengtest.fraudcheckmodelreq中插入数据
            #UniqueID
            UniqueID = str(uuid.uuid1())

            #ReqJson
            ReqJson_parttou = '{"FunctionCode":"100124","CurrentTime":"20150723203212000000","MsgBody":{"bank_cart":"12345","reasonno":"04","blackBox":"abc","ip":"192.168.1.122","account_login":"test123","loanType":"99","currency":"23232","loanMoney":10000.00,"loanTimeLimit":12,"applyDate":"2015-08-01","assureType":"D","creditAddress":"北京","is_student":0,"is_first_time":1,"degree":"1","isVerify":1,"RELATION_VERIFICATION":[{"relation_name":"陈刚3","relation_phone":"18675559750"}],'
            ReqJson_partend = '}}'
            ReqJson_part = '"UniqueID":"' + UniqueID + '","user_id":"' + str(userdata_rows[n][0]) + '","ProjectId":"' + str(userdata_rows[n][1]) + '","identity_card":"' + str(userdata_rows[n][2]) + '","idtype":"' + str(userdata_rows[n][3]) + '","mobile_phone":"' + str(userdata_rows[n][5]) + '","name":"' + str(userdata_rows[n][4]) +'"'
            ReqJson = ReqJson_parttou + ReqJson_part + ReqJson_partend
            print 'ReqJson',ReqJson
            ReqJson = base64.b64encode(ReqJson)
            print 'ReqJsonbase64:',ReqJson

            #插入数据库
            cur.execute("INSERT INTO fraudcheckmodelreq(UniqueID, ReqJson, enFraudCheckModelType, ReqTime, enFraudCheckHandleStatus) VALUES(%s, %s, %s, %s, %s)", (UniqueID,ReqJson,enFraudCheckModelType,ReqTime,enFraudCheckHandleStatus))
            #自增循环变量
            n = n + 1
    else:
        print 'functioncode is error!'

    conn.commit()
    cur.close()
    conn.close()
    return 0

if __name__ == '__main__':
    Batch_adddata_pctest(100122,100)
