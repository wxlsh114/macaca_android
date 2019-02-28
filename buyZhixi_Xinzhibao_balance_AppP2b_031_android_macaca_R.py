#coding=utf-8
from macaca import WebDriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.action_chains import ActionChains


desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'kenzo',
        #'udid':'192.168.56.101:5555',
        'app': os.path.abspath('/Users/samwang/Desktop/macaca_android/51p2b_debug_2.2.3.apk'),
        'appPackage': 'com.richfinancial.pujiaosuo',
        'unicodeKeyboard': 'true',
        'resetKeyboard': 'true',
        'fullReset': 'true',       
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class AppP2b(unittest.TestCase):
    def setUp(self):
        # set up macaca
        self.driver = WebDriver(desired_caps, server_url)
        self.driver.init()
        sleep(5)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def buy_Zhixi(self):
        driver=self.driver       

        driver.touch('drag',{'fromX':950,'fromY':1600,'toX':50,'toY':1600})
        sleep(4)
        driver.touch('drag',{'fromX':950,'fromY':1600,'toX':50,'toY':1600})
        sleep(4)
        driver.touch('drag',{'fromX':950,'fromY':1600,'toX':50,'toY':1600})
        sleep(4)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/welcome_button").click()
        sleep(5)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/tv_title_view_left").click()
        sleep(5)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/phone").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/phone").clear()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/phone").send_keys("13918647830")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").send_keys("0422wxl")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/login").click()
        sleep(5)
        cancel=driver.elements_by_class_name("android.widget.Button")
        cancel[0].click()
        sleep(3)
        inv = driver.element_by_name("投资")
        inv.click()
        sleep(3)
        #智息双全
        driver.element_by_name("智息双全测试").click()
        sleep(3)
        driver.element_by_name("立即投资").click()
        sleep(3)
        amount=driver.element_by_id("com.richfinancial.pujiaosuo:id/editbox")
        amount.click()
        amount.clear()
        amount.send_keys("10300")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/invest_mothed").click()
        sleep(2)
        #driver.element_by_name("薪智宝（元）").click()
        driver.touch('tap',{'x':520,'y':1400})
        sleep(2)
        #driver.element_by_id("com.richfinancial.pujiaosuo:id/xieyi_check").click()
        driver.element_by_name("我同意").click()
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/pay_now").click()
        sleep(5)
        driver.element_by_name("我的").click()
        sleep(4)
        driver.element_by_name("优贝赚呗投资记录").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf2="./"+now+"_031_inv_records_macaca_R.png"
        driver.save_screenshot(sf2)
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/item_title").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf3="./"+now+"_031_inv_detail_macaca_R.png"
        driver.save_screenshot(sf3)
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        #scroll to the tail page
        #driver.swipe(520,1700,520,600,1000)
        driver.touch('drag',{'fromX':520,'fromY':1600,'toX':520,'toY':900})
        sleep(2)
        driver.element_by_name("我的薪智宝").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf4="./"+now+"_031_xinzhibao_macaca_R.png"
        driver.save_screenshot(sf4)
        sleep(3)
                    
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b("buy_Zhixi"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename="./"+now+"_031_result_macaca_R.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment android6.0.1(投资智息双全(用薪智宝+账户余额支付) test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
