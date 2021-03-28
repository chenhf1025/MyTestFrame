# encoding:utf-8
from selenium.webdriver import *
import os,time
from  selenium.webdriver.common.action_chains import ActionChains
import traceback

#封装打开浏览器，输入网址的类

class Browser:

    def __init__(self,writer):

        self.driver=None
        self.text=''
        self.title=''
        self.writer = writer

   #打开不同浏览器函数
    def openbrowser(self,u='ch'):

       # 创建一个用来配置chrome属性的变量
        option = ChromeOptions()

        # 定义userdir获取用户目录
        userdir = os.environ['USERPROFILE'] + '\\AppData\\Local\\Google\\Chrome\\UserData'
        option.add_argument('--user-data-dir='+ userdir)

        if u=='ch'or u=='':
            executable_path='./web/lib/chromedriver.exe'
            self.driver=Chrome(executable_path,options=option)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')

        elif u=='ff':
            executable_path = './web/lib/geckodriver.exe'
            self.driver=Chrome(executable_path,options=option)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        else:

            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, "您好，目前系统不支持"+str(u)+"浏览器！")

        #self.driver.switch_to.default_content()
        #self.driver.window_handles






    #访问网址
    def geturl(self,url):
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')

        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())


    #查找click元素
    def click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())


    #查找输入框的元素，并输入值
    def input(self,xpath,value):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(str(value))
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())


    #进入iframe
    def intoiframe(self,xpath):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())

    #出iframe,出到最外层的html
    def outiframe(self):
        try:
            self.driver.switch_to.default_content()
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())




    #获取元素的text
    def gettext(self,xpath):
        try:

            self.text=self.driver.find_element_by_xpath(xpath).text
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())

    def gettitle(self):
        try:
            self.title=self.driver.title
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')

        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())

    def assertequals(self,p,value):
        try:
            p = p.replace('{text}', self.text)
            p = p.replace('{title}', self.title)
            if p==value:
                self.writer.write(self.writer.row, 7, 'PASS')
                self.writer.write(self.writer.row, 8, '')

        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, p)





    #切换窗口
    def switchwindow(self,idx=0):
        h=self.driver.window_handles
        try:
            self.driver.switch_to_window(h[int(idx)])
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, str(h))

    #关闭selenium当前定位的窗口
    def closewindow(self):
        self.driver.close()
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def moveto(self,xpath):
        actions=ActionChains(self.driver)
        try:
            ele=self.driver.find_element_by_xpath(xpath)
            #使用moveto可以实现悬停
            actions.move_to_element(ele).perform()
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())



    def excutejs(self,js):
        try:
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, str(js))

        #window.scrollBy(0,800)


    def sleep(self,t=3):
        time.sleep(int(t))
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, '')

    def quit(self):
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, '')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'Fail')
            self.writer.write(self.writer.row, 8, traceback.format_exc())

