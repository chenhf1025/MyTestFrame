# encoding:utf-8
from selenium.webdriver import *
from web.Web import Browser

browser=Browser()
browser.openbrowser()
browser.geturl('http://www.testingedu.com.cn:8000/index.php')

#登录页面
def login(browser):
    browser.click('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
    browser.input('//*[@id="username"]','13800138006')
    browser.input('//*[@id="password"]','123456')
    browser.input('//*[@id="verify_code"]','11111')
    browser.click('//*[@id="loginform"]/div/div[6]/a')
    browser.sleep(4)
    browser.gettext('/html/body/div[1]/div/div/div/div[2]/a[2]')

    if browser.text=='安全退出':
        print('pass')
    else:
        print('fail')
#个人信息上传头像
def userinfo(browser):
    browser.click('/html/body/div[3]/div/div[2]/div[1]/div/ul[4]/li[2]/a')
    browser.click('//*[@id="preview"]')
    browser.intoiframe('//*[@id="layui-layer-iframe1"]')
    browser.input('//*[@id="filePicker"]/div[2]/input','C:\\Users\\10217\\Desktop\\地鼠.png')
    browser.outiframe()
    browser.click('//*[@id="layui-layer1"]/span[1]/a[3]')

    browser.click('/html/body/div[1]/div/div/ul/li[5]/a')

    browser.switchwindow(1)
    browser.sleep(3)


login(browser)
userinfo(browser)

browser.gettitle()
print(browser.title)
browser.closewindow()
browser.sleep()
browser.quit()