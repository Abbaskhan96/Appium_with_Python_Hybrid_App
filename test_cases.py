import pytest

# Main test case file
from Apps.Airmirror.airmirror import *
from Apps.flipkart.flipkart import *
from Apps.contacts.contacts import *
from Apps.Daraz.Daraz import *
from Apps.general_store.general_store import  *



@pytest.mark.pop
def test01_signin(airmirror_fixture):
    try:
        app_1_obj_2= airmirror(airmirror_fixture)
        app_1_obj_2.signin()

    except Exception as e:
        screenshot(e)
        print(e)


@pytest.mark.bcd1
def test02_signup(airmirror_fixture):
    try:
        app_1_obj_2= airmirror(airmirror_fixture)
        app_1_obj_2.signup()

    except Exception as e:
        screenshot(e)
        print(e)



def test03_flipkart_Mobile_scroll(flipkart_fixture):
    try:
        flipkart=flipkart_class(flipkart_fixture)
        #flipkart.skip()
        flipkart.scrolling()

    except Exception as e:
        screenshot(e)
        print(e)


@pytest.mark.marking
def test04_contact(contacts_fixture):
    try:
        contact= contacts(contacts_fixture)
        contact.account_setup()
        contact.add_account()

    except Exception as e:
        screenshot(e)
        print(e)


@pytest.mark.daraz
def test05_daraz(daraz_fixture):
    try:
        daraz= daraz_class(daraz_fixture)
        daraz.login_function()
        daraz.add_products_to_cart()

    except Exception as e:
        screenshot(e)
        print(e)

@pytest.mark.store
def test06_check_validation(general_store_fixture):
    store= store_class(general_store_fixture)
    store.check_validation_on_first_page()


@pytest.mark.store
def test07_end_to_end(general_store_fixture):
    store= store_class(general_store_fixture)
    store.first_page()
    store.second_page()
    store.third_page()
    store.webview()




def main():
    try:
        test01_signin()
        test02_signup()
        test03_flipkart_Mobile_scroll()
        test04_contact()


    except Exception as Main_exception:
        print(Main_exception)


def screenshot(e):
    print("Given Error name: ", e)
    snap_time= time.strftime("%Y_%m_%d_(%H%M%S)")
    print("Current time is...",snap_time)
    # activity= driver.current_activity
    # print("Activity..,",activity)
    filename= "Failed_Snap"+snap_time
    time.sleep(3)
    # self.driver.save_screenshot("C:/Users/abbas.khan_codup/PycharmProjects/pythonProject/Failure_Screenshots/"+filename+".png")
    # print("Screenshot Saved....")
    # self.fail("TestCase is not passed....")


if __name__ == "__main__":
    main()

