#coding=utf8
from Custom_Request import *
import ExcelRW
import json

datafile = 'testdata.xlsx'
xlseng = ExcelRW.XlsEngine(datafile)
xlseng.open()

url = xlseng.readcell('Sheet1', 2, 1)
headers = xlseng.readcell('Sheet1', 2, 2)
params = xlseng.readcell('Sheet1', 2, 3)

print url
print headers
print params

headers = json.loads(headers)


#params = params.decode('utf-8')
#print params

params = params.encode("utf-8")

#params = unicode(params, "gb2312")
#params = json.loads(params)
#print params
#params = json.dumps(params)
print params

crd = Http_Custom_Request(url)
crd.set_header(headers)

r = crd.get(params)
print r
print r.status_code
print r.headers
print r.content
