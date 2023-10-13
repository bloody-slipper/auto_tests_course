from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.first_class input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.second_class input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.third_class input')
    input3.send_keys("mail@mail.com")
    # input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block div.first_class input')
    # input4.send_keys("+79876543210")
    # input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block div.second_class input')
    # input5.send_keys("Советский союз")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()