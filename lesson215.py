from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text #присваиваем найденный текст переменной
    
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    input = browser.find_element(By.ID, 'answer').send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox').click()
    option2 = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()