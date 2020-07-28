from appium import webdriver
from selenium.webdriver import ActionChains


desired_caps = {"app": r"C:\Windows\System32\notepad.exe",
                "platformName": "Windows",
                "deviceName": "WindowsPC"}

driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

menu = driver.find_element_by_name("Файл")
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.perform()

menu.click()
menu.click()

# time.sleep(2)
# submenu = driver.find_element_by_name("Создать")
# submenu.click()
text_field = driver.find_element_by_name("Текстовый редактор")
text_field.send_keys("dasda")
driver.find_element_by_name("Закрыть").click()
driver.find_element_by_xpath("//Button[@Name=\"Не сохранять\"]").click()
