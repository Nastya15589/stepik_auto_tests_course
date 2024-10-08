from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Nastya")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Salykova")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Astana")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Kazakhstan")
    button = browser.find_element(By.XPATH, ('//button[@type="submit"]'))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()