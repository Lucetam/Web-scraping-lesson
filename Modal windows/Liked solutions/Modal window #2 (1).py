from selenium import webdriver
from selenium.webdriver.common.by import By
from random import shuffle


url = 'http://parsinger.ru/blank/modal/3/index.html'

red, green = '255, 230, 230', '230, 255, 230'
color_change = "arguments[0].setAttribute('style', 'background-color: rgb({});')"

with webdriver.Chrome() as browser:
    browser.get(url)
    check_field = browser.find_element(By.ID, 'input')
    check_btn = browser.find_element(By.ID, 'check')
    res = browser.find_element(By.ID, 'result')
    btns = browser.find_elements(By.CLASS_NAME, 'buttons')
    while btns:
        shuffle(btns)
        btn = btns.pop()
        btn.click()
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        check_field.send_keys(pin)
        check_btn.click()
        if 'Неверный' not in res.text:
            print(res.text)
            browser.execute_script(color_change.format(green), btn)
            break
        else:
            browser.execute_script(color_change.format(red), btn)
    __import__('time').sleep(10)