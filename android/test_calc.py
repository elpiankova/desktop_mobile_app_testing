from appium import webdriver
# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.0",
    "deviceName": "Android",
    "avd": 'Pixel_2_API_30',
    # "UDID": "ZY223FGV24",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element(By.ID, "digit_9").click()
driver.find_element(By.ID, "op_add").click()
driver.find_element(By.ID, "digit_9").click()
# driver.find_element(By., "=").click()
# driver.find_element_by_accessibility_id("равно").click()
driver.find_element_by_accessibility_id("equals").click()
result = driver.find_element(By.ID, "result_final")
assert result.text == "18"


advance = driver.find_element_by_class_name("androidx.slidingpanelayout.widget.SlidingPaneLayout")
print(advance.location)
print(advance.size)
# advance.click()
actions = TouchAction(driver)
actions.tap()
actions.press(advance,  advance.size["width"]-5, advance.size["height"]//2)
actions.move_to(advance, 10, advance.size["height"]//2)
actions.release()
actions.perform()


# driver.tap()
driver.swipe(
    advance.size["width"]-5,
    advance.location["y"] + advance.size["height"]//2,
    10,
    advance.location["y"] + advance.size["height"]//2
)


