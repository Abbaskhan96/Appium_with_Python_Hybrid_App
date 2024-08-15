from appium.webdriver.common.appiumby import AppiumBy
import time
from Locators.locators_daraz import *


class daraz_class:

    def __init__(self, daraz_fixture):
        self.driver= daraz_fixture
        self.loc= daraz_locators()


    def login_function(self):
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.country).click()
        time.sleep(10)
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.Account).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.login).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.login_google).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.agree).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.zzic).click()
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.zzic).click()


    def add_products_to_cart(self):
        self.driver.find_element(by=AppiumBy.XPATH, value= self.loc.home).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=self.loc.all_categories).click()

