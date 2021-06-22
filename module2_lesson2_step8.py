# Задание действительно очень странное и неествественное
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os 

try: 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()    
    browser.get(link)

    option0 = browser.find_element_by_css_selector('[name="firstname"]')
    option0.send_keys('1')

    
    option1 = browser.find_element_by_css_selector('[name="lastname"]')
    option1.send_keys('1')

    option2 = browser.find_element_by_css_selector('[name="email"]')
    option2.send_keys('1')

    
    option3 = browser.find_element_by_id('file')
    option3.send_keys(file_path)

    
    option4 = browser.find_element_by_tag_name("button")
    option4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()