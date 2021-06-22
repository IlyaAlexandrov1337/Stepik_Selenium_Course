# Задание действительно очень странное и неествественное
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(x))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()    
    browser.get(link)

    option0 = browser.find_element_by_tag_name("button")
    option0.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    option1 = browser.find_element_by_id('input_value')
    x = int(option1.text)
    val = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(val)
    
    option3 = browser.find_element_by_tag_name("button")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()