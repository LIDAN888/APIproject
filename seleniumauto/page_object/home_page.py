from seleniumauto.common.read_yaml import ReadElement
from seleniumauto.page.base_object import BaseObject


class HomePage(BaseObject):
    '''定义一个全局变量，为ReadElement创建一个对象'''
    global element
    element=ReadElement('home_element.yaml')
    '''点击上侧菜单栏，跳转到对应的菜单页面，menu_name：字符串格式，菜单名，通过菜单名决定跳转到哪个菜单下；
    业务逻辑：先点上侧菜单栏，再点左侧菜单栏跳转到具体页面
    menu_name:上侧菜单管理
    page_name:产品分类'''
    def menu_bar(self,menu_name):
        self.implicitly_wait(5)
        key,value=self.find_key(element,menu_name)
        self.elements_locator(key,value).click()
    def login_out(self):
        pass
