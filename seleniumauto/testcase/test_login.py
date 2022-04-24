
from selenium import webdriver
import pytest

from seleniumauto.conftest import open_chrome
from seleniumauto.page_object.login_page import LoginPage

@pytest.mark.run(order=1)
class TestLogin:
    def test_login(self,open_chrome):
        driver=LoginPage(open_chrome)
        driver.get_url('http://fecmalladmin.fecpx.com')
        username="test"
        password="testfecbbc123"
        text=driver.login(username,password)
        message="您好: %s"%username
        assert message in text



