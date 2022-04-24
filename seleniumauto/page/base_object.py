from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:
    # def __init__(self,driver:webdriver = None):
    #     if driver is None:
    #         self.driver=webdriver.Chrome()
    #     else:
    #         self.driver=driver
    def __init__(self,driver):
        self.driver=driver
    def get_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
    def find_key(self,obj,item):
        key,value=obj.read_element(item)
        return key,value
    def elements_locator(self,key,value):
        if key == 'CSS_SELECTOR':
            return self.driver.find_element(By.CSS_SELECTOR,value)
        elif key == 'ID':
            return self.driver.find_element(By.ID,value)
        elif key == 'NAME':
            return self.driver.find_element(By.NAME,value)
        elif key == 'LINK_TEXT':
            return self.driver.find_element(By.LINK_TEXT,value)
        elif key == 'PARTRIAL_LINK_TEXT':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
        elif key == 'XPATH':
            return self.driver.find_element(By.XPATH,value)
        elif key == 'CLASS_NAME':
            return self.driver.find_element(By.CLASS_NAME,value)
        elif key == 'TAG_NAME':
            return self.driver.find_element(By.TAG_NAME,value)
    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)
    def display_wait(self,time,time_cell):
        WebDriverWait(self.driver,time,time_cell)
    def select_locate(self,locator,select_type,select_value):
        #locator=self.driver.find_element(By.TAG_NAME,'select')
        '''如果元素不可见先处理成可见'''
        if locator.is_displayed() is False:
            js='document.querySelectorAll("select")[2].style.display="block"'
            self.driver.execute_script(js)
        '''name:index,value,text
            locato:元素识别的返回值'''
        if select_type == 'index':
            Select(locator).select_by_index(select_value)
        elif select_type == 'value':
            Select(locator).select_by_value(select_value)
        elif select_type == 'text':
            Select(locator).select_by_visible_text(select_value)
            Select()
    def js_handle(self,js):
        self.driver.execute_script(js)


