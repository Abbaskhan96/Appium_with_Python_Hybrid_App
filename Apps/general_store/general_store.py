from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import time
from Locators.locators_general_store import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import appium.webdriver.extensions.android.nativekey as nativekey
import random


class store_class:

    def __init__(self, general_store_fixture):
        self.driver= general_store_fixture
        self.loc= general_store_locators


    def check_validation_on_first_page(self):
        self.driver.find_element(by=AppiumBy.XPATH,value=self.loc.Female).click()
        self.driver.find_element(by=AppiumBy.XPATH,value=self.loc.Male).click()
        self.driver.find_element(by=AppiumBy.XPATH,value=self.loc.lets_shop).click()

        name_error_text=self.driver.find_element(by=AppiumBy.XPATH,value=self.loc.name_error).text

        assert name_error_text == "Please enter your name"

    def first_page(self):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.country).click()
        random_num= random.randint(1,10)
        [self.driver.swipe(411,1685,411,664,500) for i in range(random_num)]
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.select_country).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.name).send_keys("Abbas")
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.lets_shop).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.back_btn).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.lets_shop).click()


    def second_page(self):

        # self.ATC(["Jordan 6 Rings","PG 3","Converse All Star"])

        with open("C:/Users/abbas.khan_codup/PycharmProjects/pythonProject/Apps/general_store/product_names.txt", "r") as f:
            products = [product_names.strip() for product_names in f.readlines()]

        self.ATC(products)

    def ATC(self, product_names):
        i=0
        for product in product_names:

            while i<11:
                try:
                    value = f"//android.support.v7.widget.RecyclerView[@resource-id='com.androidsample.generalstore:id/rvProductList']/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productName' and @text='{product}']"
                    self.driver.find_element(by=AppiumBy.XPATH, value= value)
                    print(product, "product is slciked.")
                    ATC= "//android.support.v7.widget.RecyclerView[@resource-id='com.androidsample.generalstore:id/rvProductList']/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart']"
                    time.sleep(1)
                    self.driver.find_element(by=AppiumBy.XPATH, value=ATC).click()
                    [self.driver.swipe(140, 600, 140, 3000, 500) for j in range(3)]
                    i=i+1
                    break


                except NoSuchElementException:
                    self.driver.swipe(140,1333,140,900,300)
                    i=i+1
                    if i==11:
                        [self.driver.swipe(140,600, 140, 3000, 100) for k in range(2)]
                        #self.ATC(product_name)

            i=0



    def third_page(self):
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.cart_btn).click()

        self.driver.execute_script('mobile: longClickGesture', {'x': 520, 'y': 1720, 'duration': 2000})
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.close_terms).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.web_btn).click()
        time.sleep(3)


    def webview(self):
        context=self.driver.contexts
        #self.driver.context('WEBVIEW_com.androidsample.generalstore')
        self.driver.switch_to.context(context[1])

        self.driver.find_element(By.XPATH, "//textarea[@name='q']").click()
        s="Test Automation Hybrid App"
        self.driver.hide_keyboard()


        self.driver.find_element(By.XPATH, "//textarea[@name='q']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys(s)
        #self.driver.find_element(By.XPATH, "//android.widget.EditText").getKeyboard().sendKeys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys(Keys.ENTER)

        android_key = nativekey.AndroidKey
        value_back = 'BACK'  # use TAB key as an example
        value_home= 'HOME'

        keycode_back = android_key.__dict__.get(value_back, None)
        keycode_home = android_key.__dict__.get(value_home, None)
        #print(f"key={value_back}, keycode={keycode_back}")

        # driver init code is skipped
        self.driver.press_keycode(keycode_back)
        self.driver.press_keycode(keycode_home)
        self.driver.quit()

