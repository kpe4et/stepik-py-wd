import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("kot@mot.com")
    
    cur_dir = os.path.dirname(__file__)
    needed_file = os.path.join(cur_dir, 'new.txt')
    browser.find_element(By.ID, "file").send_keys(needed_file)
    

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()