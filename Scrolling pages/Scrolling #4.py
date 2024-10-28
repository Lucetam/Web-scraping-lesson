from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/scroll/2/index.html'
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    numbers = []
    browser.get(url=url)
    action = ActionChains(browser)
    for div in browser.find_elements(By.XPATH, '//div[@class="item"]'):
        checkbox = div.find_element(By.TAG_NAME, 'input')
        action.scroll_to_element(checkbox).move_to_element(checkbox).click().perform()
        if temp := div.find_element(By.TAG_NAME, 'span').text:
            numbers.append(int(temp))
    print(sum(numbers))
