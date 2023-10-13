from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100') #ждем 15 сек пока цена не будет равна 100
        )
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 150)", "") 
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'solve').click() 

finally:
    time.sleep(20)
    browser.quit()