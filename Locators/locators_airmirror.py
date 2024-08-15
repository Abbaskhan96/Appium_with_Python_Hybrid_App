

class locators_airmirror:

    #=====SIGN in - LOCATORS=================================>>>>>>>>>>>>>>

    signin='//android.widget.TextView[@resource-id="com.sand.airmirror:id/tvLogin"]'
    signin_email='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Email"]'
    signin_password='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Password"]'

    login_btn='com.sand.airmirror:id/btnLogin'
    error_msg='com.sand.airmirror:id/tvMessage'
    ok_btn='com.sand.airmirror:id/tvOK'


    #=====SIGN UP - LOCATORS================================>>>>>>>>>>>>>>>>

    signup='//android.widget.TextView[@resource-id="com.sand.airmirror:id/tvRegister"]'
    signup_email='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Email"]'
    signup_password='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Password"]'
    signup_re_password='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Enter password again"]'
    nickname='//android.widget.EditText[@resource-id="com.sand.airmirror:id/content" and @text="Nick name"]'
    register_btn='//android.widget.Button[@resource-id="com.sand.airmirror:id/btnRegister"]'
    not_matched_msg='//android.widget.TextView[@resource-id="com.sand.airmirror:id/description" and @text="Passwords do not match."]'