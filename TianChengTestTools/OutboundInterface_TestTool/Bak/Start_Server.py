#coding=utf8
from Custom_Server import *

host = '192.168.1.64'    #服务器IP
port = 8002         #端口
request_path = '/niiwoo-open-api/openApiController/'  #请求URL路径

#请求参数
request_params = '{"CurPage":"1","EndTime":"20150811133308587608","FunctionCode":"1001000001","LastUpdateTime":"19900101010101000000","PageNum":"20","SessionId":"","SystemId":"tiancheng","Token":"tianchengtoken"}'

#响应数据文件
response_filename = '.\\UserBasicInfo_Sync\\response_data.json'
response_filename1 = '.\\UserBasicInfo_Sync\\frist.json'
response_filename2 = '.\\UserBasicInfo_Sync\\test.json'
response_filename3 = '.\\UserBasicInfo_Sync\\ttt.json'

#启动服务
main(host,port,request_path,request_params,response_filename3)
#main(host,port,request_path,request_params,response_filename2)
