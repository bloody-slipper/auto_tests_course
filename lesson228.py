from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME,'firstname').send_keys('Vanya')
    browser.find_element(By.NAME,'lastname').send_keys('Vanechkin')
    browser.find_element(By.NAME,'email').send_keys('vanya@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
