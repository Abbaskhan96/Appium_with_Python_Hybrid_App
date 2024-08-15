class general_store_locators:

    #=======First Page=================
    country="//android.widget.TextView[@resource-id='android:id/text1']"
    #select_country="//android.widget.TextView[@resource-id='android:id/text1' and @text='Afghanistan']"
    select_country="//android.widget.ListView/android.widget.TextView[5]"
    name="//android.widget.EditText[@resource-id='com.androidsample.generalstore:id/nameField']"
    lets_shop="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnLetsShop']"
    back_btn="//android.widget.ImageButton[@resource-id='com.androidsample.generalstore:id/appbar_btn_back']"

    #gender
    Female="//android.widget.RadioButton[@resource-id='com.androidsample.generalstore:id/radioFemale']"
    Male="//android.widget.RadioButton[@resource-id='com.androidsample.generalstore:id/radioMale']"


    #Errors that needs validate on first page
    name_error="//android.widget.Toast[@text='Please enter your name']"


    #=====Second Page=================
    product_1_cart="(//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart'])[1]"
    product_2_cart="(//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart'])[2]"
    cart_btn="//android.widget.ImageButton[@resource-id='com.androidsample.generalstore:id/appbar_btn_cart']"

    terms_text="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/termsButton']"
    close_terms="//android.widget.Button[@resource-id='android:id/button1']"
    web_btn="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnProceed']"