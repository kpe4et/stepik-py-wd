import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

browser.find_element(By.ID, "book").click()

WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input_value")))
x = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)

browser.quit()