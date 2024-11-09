from tqdm import tqdm
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/selenium/5.7/4/index.html')
    action = ActionChains(browser)
    el_for_scroll = browser.find_element(By.ID, 'main_container')
    scroll_origin = ScrollOrigin.from_element(el_for_scroll)
    sleep(1)
    for _ in range(100):
        action.scroll_from_origin(scroll_origin, 0, 100).perform()
    for row in tqdm(el_for_scroll.find_elements(By.TAG_NAME, 'div'), desc='Обход строки'):
        for box in row.find_elements(By.TAG_NAME, 'input'):
            if int(box.get_attribute('value')) % 2 == 0:
                action.move_to_element(box).click().perform()
    sleep(1)
    action.scroll_to_element(browser.find_element(By.CLASS_NAME, 'alert_button')).move_to_element(
        browser.find_element(By.CLASS_NAME, 'alert_button')).click().perform()
    sleep(1)
    print(browser.switch_to.alert.text)
    sleep(2)
