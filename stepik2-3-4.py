import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = browser.switch_to.alert
    alert.accept()
    

    x = browser.find_element(By.ID, "input_value").text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, "answer").send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()