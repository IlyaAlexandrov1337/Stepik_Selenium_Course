# Задание действительно очень странное и неествественное
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return str(x + y)


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()    
    browser.get(link)

    option1 = browser.find_element_by_id("num1")
    x = option1.text
    x = int(x)

    option2 = browser.find_element_by_id("num2")
    y = option2.text
    y = int(y)

    sum = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)
    
    option3 = browser.find_element_by_tag_name("button")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()