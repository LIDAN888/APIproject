import os
import sys
import copy

import yaml
class ReadElement:
    def __init__(self,filename):
        with open(r'E:\APIproject\seleniumauto\page_element\%s'%filename,'r',encoding='utf-8') as f:
            self.data=yaml.load(stream=f,Loader=yaml.FullLoader)
        f.close()
    def read_element(self,item1,item2=None):#item是yaml文件中的key,如果value是字典，需要再进行下一步处理
        if item1 in self.data:
            if type(self.data.get(item1)) is dict:
                self.data=self.data.get(item1)
                item1=item2
                return self.read_element(item1)
            else:
                data=self.data.get(item1)
                key,value=data.split('==')
                return key,value

if __name__ == '__main__':
    element=ReadElement('home_element.yaml')
    key,value=element.read_element("上侧菜单管理","产品分类")
    print(key,value)
    key, value = element.read_element("产品分类", "产品管理")
    print(key,value)



