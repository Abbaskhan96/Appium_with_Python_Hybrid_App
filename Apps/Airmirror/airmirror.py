from appium.webdriver.common.appiumby import AppiumBy
import time
from Locators.locators_airmirror import *


class airmirror:

    def __init__(self, airmirror_fixture):
        self.driver= airmirror_fixture
        self.loc= locators_airmirror()


    def signin(self):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signin).click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signin_email).send_keys("abbas.khan@codup.co")
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.signin_password).send_keys("12345")

        self.driver.find_element(by=AppiumBy.ID, value= self.loc.login_btn).click()
        msg= self.driver.find_element(by= AppiumBy.ID, value= self.loc.error_msg).text
        assert msg == 'Failed to sign in. Email or password is incorrect. (-10001)'

        self.driver.find_element(by=AppiumBy.ID, value= self.loc.ok_btn).click()


    def signup(self):
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signup).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signup_email).send_keys("abbas.khan@codup.co")
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signup_password).send_keys("abbas$$$###")
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.signup_re_password).send_keys("abbas")
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.nickname).send_keys("abbas")
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.register_btn).click()
        msg=self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.not_matched_msg).text
        assert msg == 'Passwords do not match.'
