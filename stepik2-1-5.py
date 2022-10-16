import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.find_element(By.ID, "robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()