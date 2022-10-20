from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button_exists_and_some_language_cheks(browser):
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
    elif language == 'fr':
        assert assertion_text == "Ajouter au panier"
    else: 
        assert len(assertion_text) > 0, "Button not found"
