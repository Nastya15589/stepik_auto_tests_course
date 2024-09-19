from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "num1")
    num1 = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)
    def summ(num1, num2):
      return str(num1 + num2)
    total = summ(num1, num2)
    
    select = Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select"))
    select.select_by_value(total)
    
    button = browser.find_element(By.CSS_SELECTOR, ('button[type="submit"]'))
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()