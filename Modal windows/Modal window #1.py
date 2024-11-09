from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/selenium/5.8/1/index.html')
    act = ActionChains(browser)
    for tag in browser.find_elements(By.TAG_NAME, 'input'):
        tag.click()
        alert = browser.switch_to.alert
        alert.accept()
        if text := browser.find_element(By.ID, 'result').text:
            print(text)
            break
