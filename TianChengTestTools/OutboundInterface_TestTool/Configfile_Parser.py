#coding=utf-8
#######################################################
#filename:Configfile_Parser.py
#author:defias
#date:2015-7
#function:
#######################################################
import configparser

class Configfile_Parser(object):
    '''解析配置文件'''

    def __init__(self, ini_file):
        self.config = configparser.ConfigParser()
        #从配置文件中读取接口服务器IP、域名，端口等信息'''
        self.config.read(ini_file)

    def get_host(self, *section):
        '''指定配置段获取主机'''
        sec_len = len(section)
        if 0 == sec_len:
            return str(self.config.get('DEFAULT', 'host'))
        elif 1 == sec_len:
            return str(self.config.get(section[0], 'host'))
        else:
            return -1

    def get_port(self, *section):
        '''指定配置段获取端口号'''
        sec_len = len(section)
        if 0 == sec_len:
            return str(self.config.get('DEFAULT', 'port'))
        elif 1 == sec_len:
            return str(self.config.get(section[0], 'port'))
        else:
            return -1

    def get_runmode(self, *section):
        '''指定配置段获取运行模式'''
        sec_len = len(section)
        if 0 == sec_len:
            return str(self.config.get('DEFAULT', 'runmode'))
        elif 1 == sec_len:
            return str(self.config.get(section[0], 'runmode'))
        else:
            return -1

    def get_index(self, *section):
        '''指定配置段获取待执行的列表'''
        sec_len = len(section)
        if 0 == sec_len:
            return eval(str(self.config.get('DEFAULT', 'index')))
        elif 1 == sec_len:
            return eval(str(self.config.get(section[0], 'index')))
        else:
            return -1

    def get_unindex(self, *section):
        '''指定配置段获取不执行的列表'''
        sec_len = len(section)
        if 0 == sec_len:
            return eval(str(self.config.get('DEFAULT', 'unindex')))
        elif 1 == sec_len:
            return eval(str(self.config.get(section[0], 'unindex')))
        else:
            return -1

    def get_testfile_coln(self, *section):
        '''指定配置段获取测试文件列定义列表'''
        sec_len = len(section)
        if 0 == sec_len:
            return eval(str(self.config.get('DEFAULT', 'testfile_coln')))
        elif 1 == sec_len:
            return eval(str(self.config.get(section[0], 'testfile_coln')))
        else:
            print cc.get_index()
            return -1

if __name__ == '__main__':
    cc = Configfile_Parser("..\\..\\conf\\Conf.ini")
    print cc.get_host()
    print cc.get_index()
    #print cc.get_port()
