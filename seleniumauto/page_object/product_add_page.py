import time

from seleniumauto.common.read_yaml import ReadElement
from seleniumauto.page.base_object import BaseObject


class ProductAddPage(BaseObject):
    global element
    element=ReadElement('addinfo_element.yaml')
    def add_basic_info(self,product_name,left_scroll,top_scroll):
        key,value=element.read_element('产品名字')
        self.elements_locator(key,value).send_keys(product_name)
        time.sleep(5)
        key,value=element.read_element('添加页面滚动条')
        self.scroll_to(key,value,left_scroll,top_scroll)
    def add_price(self,*args):
        key,value=element.read_element('价格部分')
        self.elements_locator(key,value).click()
        key,value=element.read_element('等级价格')
        self.elements_locator(key,value).click()
        key,value=element.read_element('等级价格个数第一行')
        self.elements_locator(key,value).send_keys(args[0])
        key,value=element.read_element('等级价格价格第一行')
        self.elements_locator(key,value).send_keys(args[1])
        key,value=element.read_element('等级价格')
        self.elements_locator(key,value).click()
        key,value=element.read_element('等级价格个数第二行')
        self.elements_locator(key,value).send_keys(args[2])
        key,value=element.read_element('等级价格价格第二行')
        self.elements_locator(key,value).send_keys(args[3])
    def add_meta(self):
        pass
    def add_picture(self):
        pass
    def add_kind_info(self):
        key,value=element.read_element('分类信息')
        self.elements_locator(key,value).click()
        self.implicitly_wait(3)
        key,value=element.read_element('分类信息复选框')
        locator=self.elements_find(key,value)
        locator[0].click()
        key,value=element.read_element('保存按钮')
        self.elements_locator(key,value).click()
        self.implicitly_wait(3)
        self.alert_handle('accept')
        self.screen_shot(r"E:\APIproject\seleniumauto\screen_shot\1.png")