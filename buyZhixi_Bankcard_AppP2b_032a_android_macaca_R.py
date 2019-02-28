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
        sleep(4)
        
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
        driver.element_by_id("com.richfinancial.pujiaosuo:id/phone").send_keys("18811446922")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").click()
        driver.element_by_id("com.richfinancial.pujiaosuo:id/password").send_keys("0422wxl")
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/login").click()
        sleep(4)
        cancel=driver.elements_by_class_name("android.widget.Button")
        cancel[0].click()
        sleep(3)
        inv = driver.element_by_name("投资")
        inv.click()
        sleep(4)
        #Zhixi
        driver.element_by_name("智息双全测试").click()
        sleep(4)
        driver.element_by_name("立即投资").click()
        sleep(4)
        amount=driver.element_by_id("com.richfinancial.pujiaosuo:id/editbox")
        amount.click()
        amount.send_keys("3700")
        sleep(2)
        #payment method
        driver.element_by_id("com.richfinancial.pujiaosuo:id/invest_mothed").click()
        sleep(3)
        driver.element_by_name("建设银行（尾号5512）").click()
        sleep(2)
        #I agree
        driver.element_by_name("我同意").click()
        sleep(2)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/pay_now").click()
        sleep(2)
        icode=driver.element_by_id("com.richfinancial.pujiaosuo:id/code")
        icode.click()
        icode.send_keys("abcd")
        sleep(2)
        driver.element_by_name("获取").click()
        sleep(5)
        mcode=driver.element_by_id("com.richfinancial.pujiaosuo:id/msmcode")
        mcode.click()
        mcode.send_keys("123456")
        sleep(1)
        #I agree
        driver.element_by_name("我同意").click()
        sleep(2)
        #queding
        driver.element_by_id("com.richfinancial.pujiaosuo:id/next").click()
        sleep(55)
        #确定
        driver.element_by_id("com.richfinancial.pujiaosuo:id/btn_complete").click()
        sleep(3)
        driver.element_by_name("我的").click()
        sleep(4)
        driver.element_by_name("优贝赚呗投资记录").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf2="./"+now+"_032a_inv_records_macaca_R.png"
        driver.save_screenshot(sf2)
        sleep(3)
        #t=driver.find_element_by_id("com.richfinancial.pujiaosuo:id/channel").text
        #assert '含手续费0.00元' in t
        driver.element_by_id("com.richfinancial.pujiaosuo:id/item_title").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf3="./"+now+"_032a_inv_detail_macaca_R.png"
        driver.save_screenshot(sf3)
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        driver.element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        driver.touch('drag',{'fromX':540,'fromY':1000,'toX':540,'toY':300})
        sleep(2)
        driver.element_by_name("账户余额（元）").click()
        sleep(4)
        driver.element_by_name("查看余额明细").click()
        sleep(3)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf4="./"+now+"_032a_recharge_macaca_R.png"
        driver.save_screenshot(sf4)
        sleep(3)
        """
        t2=driver.element_by_id("com.richfinancial.pujiaosuo:id/channel").text
        assert '融宝支付' in t2
        """
        driver.element_by_id("com.richfinancial.pujiaosuo:id/channel").click()
        sleep(4)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf5="./"+now+"_032a_recharge_detail_macaca_R.png"
        driver.save_screenshot(sf5)
        sleep(3)
                    
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b("buy_Zhixi"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename="./"+now+"_032a_result_macaca_R.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment android6.0.1[投资智息双全(用银行卡支付：融宝支付)] test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
