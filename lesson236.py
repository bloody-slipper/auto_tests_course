from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    new_window = browser.window_handles[1] #присваиваем переменной новое коно
    browser.switch_to.window(new_window) #переключаемся на новую вкладку
    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
