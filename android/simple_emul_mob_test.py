# To successfully run this test you should have connected android device
# This script will just open Calculator Android app on your android device

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {
    "automationName": "UiAutomator2",
    # "app": Note that this capability is not required for Android if you specify appPackage and appActivity capabilities (see below).
    # "browserName": "Chrome" # For web tests
    'platformName': 'Android',
    'platformVersion': '11.0',
    "avd": 'Pixel_2_API_30',
    # "UDID": "emulator-5554",
    'deviceName': 'Android',
    'appPackage': 'com.google.android.calculator',
    'appActivity': 'com.android.calculator2.Calculator'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

button_2 = driver.find_element(By.ID, "digit_2")
button_2.click()

# driver.quit()
