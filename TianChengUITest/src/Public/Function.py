#coding=utf-8
#######################################################
#filename:Function.py
#author:defias
#date:2016-4-27
#function: public function
#######################################################
from io import StringIO
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

memdata = StringIO()  #内存数据

def is_chinese(ustring):
    """判断一个unicode是否是汉字"""
    for uch in ustring.decode('utf-8'):
        if u'\u4e00' <= uch <= u'\u9fff':
            return True
    return False

def ch2unicode(data):
    '''
    转换为unicode
    '''
    if type(data) is unicode:
        return data
    if type(data) is not str:
        data = str(data)
    try:
        data = unicode(data, 'utf-8')
    except UnicodeDecodeError:
        data = unicode(data, 'gbk')
    return data

def DealEnviron():
    '''处理环境变量'''
    TCWT_HOME = os.getenv('TCWT_HOME')
    if TCWT_HOME is None:
        raise('Environment variable: TCWT_HOME is not set! eg: D:\CODE\Code\TianChengUITest ')
    memdata.write(ch2unicode(TCWT_HOME))



if __name__ == '__main__':
    print is_chinese(u'sdfsdfsd')
