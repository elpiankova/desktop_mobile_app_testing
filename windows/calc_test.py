from appium import webdriver
from appium.webdriver.common.mobileby import By


desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
# r"C:\Windows\System32\notepad.exe"

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities=desired_caps)


# driver.find_element_by_name()
# driver.find_element_by_xpath()
# driver.find_element_by_class_name()
el = driver.find_element_by_accessibility_id("num7Button")
el.click()

el2 = driver.find_element_by_xpath("//Button[@Name=\"Seven\"]")
el2.click()

result = driver.find_element_by_accessibility_id("CalculatorResults")
print(result.text)
driver.quit()
