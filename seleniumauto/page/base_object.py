

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    '''定位单个元素'''
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
    '''定位一组元素'''
    def elements_find(self,key,value):
        if key == 'CSS_SELECTOR':
            return self.driver.find_elements(By.CSS_SELECTOR,value)
        elif key == 'ID':
            return self.driver.find_elements(By.ID,value)
        elif key == 'NAME':
            return self.driver.find_elements(By.NAME,value)
        elif key == 'LINK_TEXT':
            return self.driver.find_elements(By.LINK_TEXT,value)
        elif key == 'PARTRIAL_LINK_TEXT':
            return self.driver.find_elements(By.PARTIAL_LINK_TEXT,value)
        elif key == 'XPATH':
            return self.driver.find_elements(By.XPATH,value)
        elif key == 'CLASS_NAME':
            return self.driver.find_elements(By.CLASS_NAME,value)
        elif key == 'TAG_NAME':
            return self.driver.find_elements(By.TAG_NAME,value)
    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)
    def display_wait(self,time,key,value):
        if key=='XPATH':
            wait=WebDriverWait(self.driver,time).until(EC.presence_of_element_located((By.XPATH,value)))
        return wait
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
    def js_handle(self,js):
        self.driver.execute_script(js)
    '''处理内嵌滚动条'''
    def scroll_to(self,key,value,left_gap,top_gap):

        if key=='CSS_SELECTOR':
            js='document.querySelector("%s").scrollTo(%s,%s)'%(value,left_gap,top_gap)
            self.driver.execute_script(js)
        elif key=='CLASS_NAME':
            js = 'document.getElementsByClassName("%s").scrollTop=%d' % (value,top_gap)
            self.driver.execute_script(js)
    '''处理一般滚动条'''
    def window_scroll(self):
        js='window.scrollTo(0,1000)'
        self.driver.execute_script(js)
    '''处理弹框'''
    def alert_handle(self,handle):
        if handle=='accept':
            self.driver.switch_to.alert.accept()
        elif handle=='dismiss':
            self.driver.switch_to.alert.dismiss()
        elif handle=='text':
            return self.driver.switch_to.alert.text
    def screen_shot(self,filename):
        self.driver.get_screenshot_as_file(filename)



