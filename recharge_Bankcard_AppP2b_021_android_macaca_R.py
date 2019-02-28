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
        'udid':'7c72478d',
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

    def reCharge(self):
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
        driver.element_by_id("com.richfinancial.pujiaosuo:id/phone").send_keys("18811446922")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").send_keys("0422wxl")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/login").click()
        sleep(3)
        cancel=driver.elements_by_class_name("android.widget.Button")
        cancel[0].click()
        sleep(3)
        my = driver.element_by_name("我的")
        my.click()
        sleep(3)
        balance = driver.element_by_name("账户余额（元）")
        balance.click()
        sleep(2)
        #recharge
        driver.element_by_name("充值").click()
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/recharge_money").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/recharge_money").send_keys("3988")
        driver.element_by_name("下一步").click()
        sleep(7)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/code").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/code").send_keys("abcd")
        sleep(2)
        driver.element_by_name("获取").click()
        sleep(5)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/msmcode").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/msmcode").send_keys("123456")
        sleep(2)
        driver.element_by_name("我同意").click()
        sleep(2)
        #OK
        driver.element_by_id("com.richfinancial.pujiaosuo:id/next").click()
        sleep(55)
        #确定
        driver.element_by_id("com.richfinancial.pujiaosuo:id/btn_complete").click()
        sleep(2)
        driver.element_by_name("我的").click()
        sleep(7)
        driver.element_by_name("账户余额（元）").click()
        sleep(4)
        driver.element_by_name("查看余额明细").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf2="./"+now+"_021_recharge_records_macaca_R.png"
        driver.save_screenshot(sf2)
        """
        t=driver.element_by_id("com.richfinancial.pujiaosuo:id/channel").text
        assert '融宝支付' in t
        """
        sleep(3)
                    
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b("reCharge"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename="./"+now+"_021_result_macaca_R.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment android6.0.1[银行卡充值(融宝支付)] test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
