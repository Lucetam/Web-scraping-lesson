from time import sleep
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/infiniti_scroll_3/')
    action = ActionChains(browser)
    main_divs = browser.find_elements(By.XPATH, '//div[contains(@id, "scroll-wrapper_")]')
    for bar in main_divs:
        sleep(1)
        container = bar.find_element(By.XPATH, 'div[contains(@class, "scroll-container_")]')
        scroll_origin = ScrollOrigin.from_element(container)
        for _ in range(60):
            sleep(0.1)
            action.scroll_from_origin(scroll_origin, 0, 50).perform()
    print(sum([int(num.text) for num in browser.find_elements(By.TAG_NAME, 'span')]))
