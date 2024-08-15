from appium.webdriver.common.appiumby import AppiumBy
import time
from Locators.locators_flipkart import *


# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(501, 2138)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.move_to_location(499, 564)
# actions.w3c_actions.pointer_action.release()
# actions.perform()

class flipkart_class:
    # def __init__(self, driver, capabilities, appium_server_url):
    #     self.driver=driver
    #     self.loc= flipkart_locators()
    def __init__(self, flipkart_fixture):
        self.driver= flipkart_fixture
        self.loc= flipkart_locators()


    #====== INITIALIZATION for the flipkart Application..............
        # self.driver.quit()
        # capabilities["app"] = "C:/Users/abbas.khan_codup/AppData/Local/Android/Sdk/platform-tools/flipkart.apk"
        # capabilities["appPackage"] = "com.flipkart.android"
        #
        # opt = AppiumOptions()
        # opt = opt.load_capabilities(capabilities)
        # self.driver = webdriver.WebDriver(appium_server_url, options=opt)
        # self.driver.implicitly_wait(80)


    def skip(self):
        self.driver.find_element(by=AppiumBy.ID, value=self.loc.skip_btn).click()


    def scrolling(self):
        time.sleep(30)
        #actions=self.driver.swipe(680, 1731,680, 785,1000)
        self.driver.execute_script('mobile: scrollGesture', {
            'left': 44, 'top': 44, 'width': 1011, 'height': 900,
            'direction': 'down',
            'percent': 3.0
        })

        time.sleep(2)
