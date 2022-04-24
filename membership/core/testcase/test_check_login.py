import pytest

from membership.common import read_testcase, process_data, request

@pytest.mark.checklogin
#@pytest.mark.run(order=3)
class TestCheckLogin:
    @pytest.mark.parametrize('checklogin',read_testcase.read_case('check_login.yaml'),ids=['检测登录状态'])
    def test_check_login(self,checklogin):
        print(checklogin)
        method,url,header,data,validata=process_data.ProcessData(checklogin)
        data=process_data.ExtractData(data)
        ret=request.Request().send_request(method,url,data,header)
        if ret['ret'] == 200 and ret['data']['err_code'] == 0:
            assert ret['data']['err_code'] == validata['err_code'],'已登录'


