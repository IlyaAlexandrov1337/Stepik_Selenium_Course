# Задание действительно очень странное и неествественное
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()    
    browser.get(link)

    option0 = browser.find_element_by_id("treasure")
    x = option0.get_attribute("valuex")
    x = int(x)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()


    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    option3 = browser.find_element_by_tag_name("button")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()