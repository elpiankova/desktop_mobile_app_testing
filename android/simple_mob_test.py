# To successfully run this test you should have connected android device
# This script will just open Calculator Android app on your android device


from appium import webdriver

desired_caps = {
    "automationName": "UiAutomator2", # Работает и без этого, но видимо т.к. есть UiAutomator первый, то есть это capability
    # "app": Note that this capability is not required for Android if you specify appPackage and appActivity capabilities (see below).
    # "browserName": "Chrome" # For web tests
    'platformName': 'Android',
    'platformVersion': '7.0',
    "UDID": "ZY223FGV24",
    'deviceName': 'Android',
    'appPackage': 'com.google.android.calculator',
    'appActivity': 'com.android.calculator2.Calculator'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.quit()
