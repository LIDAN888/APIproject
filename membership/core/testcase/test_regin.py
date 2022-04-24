import os

import pytest
import requests
import yaml
import json
import re
from unittest import TestCase
from membership.common import read_testcase

from membership.common import  request

from membership.common import process_data

#@pytest.mark.skip()
@pytest.mark.regin
@pytest.mark.run(order=1)
class Test_Member_Regin:
    '''
    1.创建测试用例方法，参数化
        处理参数
        发送请求
        断言状态码和token
        把token拎出来存进关联文件
    '''
    @pytest.mark.parametrize('reginfo',read_testcase.read_case('regin_data.yaml'),ids=['用户注册'])
    def test_regin_success(self,reginfo):
        method,url,header,data,validata=process_data.ProcessData(reginfo)
        ret=request.Request().send_request(method,url,data,header)
        assert ret['data']['uuid'] != ''
        seacher_uuid = re.search("'uuid':'.*?'", str(ret).replace(' ', ''))
        uuidDict = {}
        uuid = seacher_uuid.group().split(':')
        uuidDict[eval(uuid[0])] = eval(uuid[1])
        if ret['data']['uuid']:
            # uuid={'uuid':ret_json['data']['uuid']}
            read_testcase.write_data('extract_data.yaml', uuidDict)#把关联数据存进关联数据文件



