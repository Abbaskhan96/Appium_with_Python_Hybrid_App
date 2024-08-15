from appium import webdriver
from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver import ActionChains
import time




class contacts:

    def __init__(self, contacts_fixture):
        self.driver= contacts_fixture


    def account_setup(self):
        self.driver.find_element(by=AppiumBy.ID, value="com.android.contacts:id/floating_action_button").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.android.contacts:id/left_button").click()


    def add_account(self):

        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']").send_keys("Abbas")
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Last name']").send_keys("Khan")
        #self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("03353770290")
        #self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("03353770290")
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Email']").send_keys("abbas.khan@codup.co")

        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Home']").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Work']").click()
