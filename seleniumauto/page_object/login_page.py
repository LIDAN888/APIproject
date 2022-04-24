import os

from seleniumauto.common.read_yaml import ReadElement
from seleniumauto.page.base_object import BaseObject
class LoginPage(BaseObject):
    global element
    element = ReadElement("login_element.yaml")
    def login(self,username,password):
        key,value=self.find_key(element,"用户名")
        self.elements_locator(key,value).send_keys(username)
        key,value=self.find_key(element,"密码")
        self.elements_locator(key,value).send_keys(password)
        key,value=self.find_key(element,"登录按钮")
        self.elements_locator(key,value).click()
        key,value=self.find_key(element,"断言")
        validate=self.elements_locator(key,value).text
        return validate
print(os.getcwd())