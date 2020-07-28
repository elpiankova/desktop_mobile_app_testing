from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
# "Microsoft.WindowsCalculator_10.2005.23.0_x64__8wekyb3d8bbwe"

driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

window = driver.find_element_by_name('Calculator')
driver.find_element_by_name("Clear").click()
driver.find_element_by_name("Seven").click()
# result_el = driver.find_element_by_accessibility_id("CalculatorResults")
result_el = driver.find_element_by_xpath("//Text[@AutomationId=\"CalculatorResults\"]")

assert result_el.text == "Display is 7"
print(result_el.text)
print(result_el.get_attribute("ControlType"))


from appium.webdriver.common.touch_action import TouchAction

actions = TouchAction(driver)
actions.tap(driver.find_element_by_name("Seven"))
actions.long_press()
actions.perform()

driver.quit()
