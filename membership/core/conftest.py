from membership.common import read_testcase
import pytest

@pytest.fixture(scope='session',autouse=True)
def clear():
    print('清理工作开始')
    read_testcase.clear_data('extract_data.yaml')