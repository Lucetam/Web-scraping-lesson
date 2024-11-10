from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import shuffle

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/selenium/5.8/3/index.html')
    buttons = browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')
    shuffle(buttons)
    check = browser.find_element(By.XPATH, '/html/body/div/input')
    for button in tqdm(buttons):
        button_value = button.text
        check.click()
        promt = browser.switch_to.alert
        promt.send_keys(button_value)
        promt.accept()
        res = browser.find_element(By.XPATH, '/html/body/p').text
        if res != 'Неверный пин-код':
            print(res)
            break
