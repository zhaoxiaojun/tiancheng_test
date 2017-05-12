#coding=utf8
#######################################################
#filename:Config.py
#author:defias
#date:2015-11
#function: 配置类
#######################################################
import configparser
import codecs
import os

class ConfigIni(object):
    '''
    配置类
    '''
    conf_path = './Config.ini'
    if not os.path.isfile(conf_path):
        raise Exception, u'Don\'t find config file: Config.ini'
    confO = configparser.ConfigParser()
    confO.readfp(codecs.open(conf_path, "r", "utf-8"))

    @classmethod
    def get_TestcaseName(cls):
        '''
        获取测试用例名
        '''
        return cls.confO.get('DEFAULT', 'TestcaseName')

    @classmethod
    def get_Url(cls):
        '''
        获取url
        '''
        return cls.confO.get('DEFAULT', 'url')

    @classmethod
    def get_Loginuser(cls):
        '''
        获取user
        '''
        return cls.confO.get('DEFAULT', 'loginuser')

    @classmethod
    def get_Loginpasswd(cls):
        '''
        获取passwoed
        '''
        return cls.confO.get('DEFAULT', 'loginpasswd')

    @classmethod
    def get_runmode(cls):
        '''
        获取运行模式
        '''
        return cls.confO.get('DEFAULT', 'runmode')

    @classmethod
    def get_iscontrol(cls):
        '''
        获取日志控制开关
        '''
        return cls.confO.get('DEFAULT', 'iscontrol')

    @classmethod
    def get_isstdebug(cls):
        '''
        获取发布控制开关
        '''
        return cls.confO.get('DEFAULT', 'isstdebug')

    @classmethod
    def get_index(cls):
        '''
        获取待执行的用例
        '''
        return cls.confO.get('DEFAULT', 'index')

    @classmethod
    def get_unindex(cls):
        '''
        获取不执行的用例
        '''
        return cls.confO.get('DEFAULT', 'unindex')

    @classmethod
    def get_isSendMail(cls):
        '''
        是否发送邮件
        '''
        return cls.confO.get('DEFAULT', 'isSendMail')

    @classmethod
    def get_send_emladdr(cls):
        '''
        获取接收邮箱地址
        '''
        return cls.confO.get('DEFAULT', 'send_emladdr')


    @classmethod
    def get_TestEnvironment_Info(cls, section, field):
        '''
        获取配置信息
        '''
        return cls.confO.get(section, field)
