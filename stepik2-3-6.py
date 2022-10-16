import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()