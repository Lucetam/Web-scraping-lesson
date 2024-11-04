from time import sleep
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/infiniti_scroll_2/')
    action = ActionChains(browser)
    for _ in range(15):
        sleep(1)
        p_tags = browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p")
        sleep(1)
        scroll_origin = p_tags[-1]
        scroll_origin = ScrollOrigin.from_element(scroll_origin)
        action.scroll_from_origin(scroll_origin, 0, 200).perform()
        sleep(1)
    print(sum([int(num.text) for num in browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p")]))
