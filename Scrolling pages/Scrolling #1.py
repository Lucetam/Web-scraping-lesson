import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/4/index.html'
result = []

with webdriver.Chrome() as browser:
    browser.get(url=url)
    browser.fullscreen_window()
    for block in browser.find_elements(By.XPATH, '//div[@class="visibility"]'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", block)
        block.find_element(By.TAG_NAME, 'button').click()
        temp = browser.find_element(By.XPATH, '/html/body/p').text
        result.append(int(temp))

print(sum(result))
