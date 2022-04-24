import time

from seleniumauto.common.read_yaml import ReadElement
from seleniumauto.page.base_object import BaseObject
from seleniumauto.page_object.home_page import HomePage
from seleniumauto.page_object.product_add_page import ProductAddPage


class ProinfoPage(BaseObject):
    global element
    element=ReadElement("proinfo_element.yaml")
    def search_product(self,select_value,input_value,start_time,end_time):
        key,value=element.read_element('库存状态')
        self.elements_locator(key,value)
        time.sleep(3)
        key,value=element.read_element('库存状态下拉框')
        locator=self.elements_locator(key,value)
        self.select_locate(locator,'value',select_value)
        key,value=element.read_element('产品名称')
        self.elements_locator(key,value).send_keys(input_value)
        key,value=element.read_element('更新时间开始')
        js='document.getElementsByName("updated_at_gte")[1].removeAttribute("readonly")'
        self.js_handle(js)
        self.elements_locator(key,value).send_keys(start_time)
        key,value=element.read_element('更新时间结束')
        js = 'document.getElementsByName("updated_at_lt")[1].removeAttribute("readonly")'
        self.js_handle(js)
        self.elements_locator(key,value).send_keys(end_time)
        key,value=element.read_element('查询')
        self.elements_locator(key,value).click()

    def add_product(self):
        time.sleep(3)
        key,value=element.read_element('添加')
        self.elements_locator(key,value).click()

    def clear_search(self,open_chrome):
        self.implicitly_wait(5)
        HomePage(open_chrome).menu_bar('产品信息管理')
