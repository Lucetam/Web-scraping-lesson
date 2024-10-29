from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as browser:
    browser.get(url='https://parsinger.ru/infiniti_scroll_1/')
    main_div = browser.find_element(By.XPATH, '//div[@class="scroll-container"]') #Главный элемент для скрола
    actions = ActionChains(browser)
    numbers = []
    flag = True
    while flag:
        main_div.send_keys(Keys.PAGE_DOWN) #Прокручиваем страницу до конца
        sleep(0.5) #Немного времени для загрузки страницы
        try:
            flag = False if browser.find_element(By.CLASS_NAME, 'last-of-list') else True #Проверяем достигли ли мы конца страницы
        except Exception:
            pass
    sleep(1)
    for act in main_div.find_elements(By.TAG_NAME, 'span'): #Пробегаемся по полностью загруженной странице
        numbers.append(int(act.text)) #Достаем числа
        act = act.find_element(By.TAG_NAME, 'input') #Находим чекбоксы для прокликивания
        act.click() #Прокликиваем чекбокс
        sleep(0.1)
    print(sum(numbers))
