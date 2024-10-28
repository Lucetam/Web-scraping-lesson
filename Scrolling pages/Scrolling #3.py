from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://parsinger.ru/selenium/5.7/5/index.html'

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url=url)
    actions = ActionChains(browser)
    for button in browser.find_elements(By.CLASS_NAME, 'timer_button'):
        actions.click_and_hold(button).pause(float(button.text)).release(button).perform()
    sleep(2)
    print(browser.switch_to.alert.text)
