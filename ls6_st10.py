from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block>.form-group.first_class>input')
    input1.send_keys("Nastya")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block>.form-group.second_class>input')
    input2.send_keys("Sv")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block>.form-group.third_class>input')
    input3.send_keys("sv123@gmail.com")

    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    time.sleep(1)

    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    
    welcome_text = welcome_text_elt.text

    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    
    time.sleep(10)
    
    browser.quit()