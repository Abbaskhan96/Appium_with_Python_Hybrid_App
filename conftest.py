import pytest
from Apps.Airmirror.airmirror import *
from Apps.contacts.contacts import *




def setup_capabilties():
    capabilities = {"deviceName": "Android Emulator",
                    "platformName": "Android",
                    "appWaitActivity": "*",
                    "automationName": "UiAutomator2"}

    return capabilities


def load_driver(capabilities):
    opt = AppiumOptions()
    opt = opt.load_capabilities(capabilities)

    appium_server_url = 'http://localhost:4723'
    driver= webdriver.WebDriver(appium_server_url, options=opt)
    driver.implicitly_wait(2)

    return driver



#======= FIXTURE Sections========================

@pytest.fixture(scope='session')
def airmirror_fixture():

    capabilities= setup_capabilties()
    capabilities["app"] = "C:/Users/abbas.khan_codup/AppData/Local/Android/Sdk/platform-tools/Airmirror.apk"
    capabilities["appPackage"] = "com.sand.airmirror"

    driver= load_driver(capabilities)
    #app_1_obj= airmirror(driver)
    #return app_1_obj
    return driver


@pytest.fixture
def flipkart_fixture():
    capabilities= setup_capabilties()

    capabilities["app"] = "C:/Users/abbas.khan_codup/AppData/Local/Android/Sdk/platform-tools/flipkart.apk"
    capabilities["appPackage"] = "com.flipkart.android"

    driver= load_driver(capabilities)
    return driver


@pytest.fixture
def contacts_fixture():
    capabilities= setup_capabilties()

    capabilities["app"] = ""
    capabilities["appPackage"] = "com.android.contacts"
    capabilities["appActivity"] = "com.android.contacts.activities.PeopleActivity"

    driver= load_driver(capabilities)
    return driver

@pytest.fixture
def daraz_fixture():
    capabilities= setup_capabilties()
    capabilities["appPackage"] = "com.daraz.android"
    capabilities["appActivity"] = "com.lazada.activities.EnterActivity"

    driver= load_driver(capabilities)
    return driver

@pytest.fixture(scope='session')
def general_store_fixture():
    capabilities= setup_capabilties()
    capabilities["appPackage"]="com.androidsample.generalstore"
    capabilities["app"]= "C:\\Users\\abbas.khan_codup\\AppData\\Local\\Android\\Sdk\\platform-tools\\hybrid.apk"
    capabilities['setWebContentsDebuggingEnabled']='True'

    driver= load_driver(capabilities)
    return driver