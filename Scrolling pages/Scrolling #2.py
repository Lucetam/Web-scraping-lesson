from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/5.7/1/index.html'
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--start-maximized')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')


with webdriver.Chrome(options=options) as browser:
    browser.get(url=url)
    sleep(2)
    for button in browser.find_elements(By.CLASS_NAME, 'clickMe'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
    print(browser.switch_to.alert.text)
