#coding=utf8
#######################################################
#filename:Check_request.py
#author:defias
#date:2015-9
#function:
#######################################################

def check_request(self, request_path='/', request_params=''):
        # 解析请求并检查
        try:
            request_list = self.request.split(' ')
            print 'request_list:', request_list
            method = request_list[0]
            src = request_list[1]
            print 'method is:', method
            print 'src is:', src

            src_list = src.split('/')
            parse_request_params = src_list[-1]
            parse_request_path = src.replace(parse_request_params, '')
            print 'parse_request_params:', parse_request_params
            print 'parse_request_path:', parse_request_path

            # 解析请求参数
            parse_request_params_str = urllib.unquote(parse_request_params).replace('\n', '')
            print 'parse_request_params_str:', parse_request_params_str
            parse_request_params_dic = json.loads(parse_request_params_str)
            del parse_request_params_dic['EndTime']
            del parse_request_params_dic['LastUpdateTime']   # 忽略时间
            print 'parse_request_params_dic:', parse_request_params_dic

            # 预期值
            request_params_dic = json.loads(request_params)
            print 'request_params_dic:', request_params_dic
            print 'request_path:', request_path

            if (method == 'GET') and (parse_request_path == request_path):
                if set(parse_request_params_dic.items()).issubset(request_params_dic.items()):
                    print 'T'
                    return True
                else:
                    print 'FF'
                    return False
            else:
                print 'F'
                return False
        except:
            print 'exception!'
            return False
