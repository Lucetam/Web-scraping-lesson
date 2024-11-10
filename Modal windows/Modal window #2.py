from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

with webdriver.Chrome(options=options) as browser:
    browser.get(url='https://parsinger.ru/selenium/5.8/2/index.html')
    act = ActionChains(browser)
    inp = browser.find_element(By.XPATH, '//input[@type="text"]')
    check_button = browser.find_element(By.XPATH, '//input[@id="check"]')
    for tag in browser.find_elements(By.XPATH, '//input[contains(@onclick, "clickNumber")]'):
        tag.click()
        alert = browser.switch_to.alert
        code = alert.text
        alert.accept()
        inp.send_keys(code)
        check_button.click()
        text = browser.find_element(By.ID, 'result').text
        if text == 'Неверный пин-код':
            continue
        else:
            print(text)
            break
