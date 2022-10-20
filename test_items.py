from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_language(browser):
    #получаем кортеж браузер + язык и раскидываем по переменным браузер и язык
    browser, language = browser
    browser.get(link)
    assertion_text = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']").text
    if language == 'ru':
        assert assertion_text == "Добавить в корзину"
    elif language == 'en':
        assert assertion_text == "Add to basket"
    elif language == 'es':
        assert assertion_text == "Añadir al carrito"