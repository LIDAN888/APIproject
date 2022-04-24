import re

import pytest

import allure

from membership.common import read_testcase, process_data, request

@pytest.mark.login
@pytest.mark.run(order=2)
@allure.story("登录功能")
class Test_Member_Loin:
    @pytest.mark.parametrize("loginfo",read_testcase.read_case('user_login.yaml'),ids=['登录成功','账号不存在登录失败','密码错误登录失败','账号为空登录失败','密码错误登录失败'])
    def test_login(self,loginfo):
        method,url,header,data,validata=process_data.ProcessData(loginfo)
        ret=request.Request().send_request(method,url,data,header)
        '''断言'''
        if ret['ret']==200:
            if ret['data']['err_code'] == 0:
                assert ret['data']['err_code'] == validata['err_code']
                '''查找关联参数'''
                search_token = re.search("'token':'.*?'", str(ret).replace(' ', ''))
                tokenDict = {}
                token = search_token.group().split(':')
                tokenDict[eval(token[0])] = eval(token[1])
                print(tokenDict)
                if ret['data']['token']:
                    read_testcase.write_data('extract_data.yaml', tokenDict)

            elif ret['data']['err_code'] == 1:
                assert ret['data']['err_msg'] == validata['err_msg']
            elif ret['data']['err_code'] == 2:
                assert ret['data']['err_msg'] == validata['err_msg']
        elif ret['ret']==400:
            assert validata['msg'] in ret['msg']


