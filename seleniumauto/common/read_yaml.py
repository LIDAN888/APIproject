import os
import sys

import yaml
class ReadElement:
    def __init__(self,filename):
        with open(r'E:\APIproject\seleniumauto\page_element\%s'%filename,'r',encoding='utf-8') as f:
            self.data=yaml.load(stream=f,Loader=yaml.FullLoader)
        f.close()
    def read_element(self,item):#item是yaml文件中的key,如果value是字典，需要再进行下一步处理
        #print(self.data)
        if item in self.data:
                data=self.data.get(item)
                key,value=data.split('==')
                return key,value

if __name__ == '__main__':
    element=ReadElement('proinfo_element.yaml')
    key,value=element.read_element("更新时间开始")
    print(key,value)




