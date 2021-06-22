# Задание действительно очень странное и неествественное
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(x))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()    
    browser.get(link)

    option0 = browser.find_element_by_id("input_value")
    x = option0.text
    x = int(x)
    
    option3 = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    val = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(val)
    
    option3 = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()