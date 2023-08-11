import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

#Вход в аккаунт
driver.get("https://practice.automationtesting.in/")

account_bth=driver.find_element(By.ID,"menu-item-50")
account_bth.click()
time.sleep(2)
login_email=driver.find_element(By.ID,"username")
login_email.send_keys("swat1155@mail.ru")
login_password=driver.find_element(By.ID,"password")
login_password.send_keys("Grower1527_swen")
#Переход на страницу с товаром
login_bth=driver.find_element(By.NAME,"login")
login_bth.click()
time.sleep(2)
shop_bth=driver.find_element(By.ID,"menu-item-40")
shop_bth.click()
time.sleep(2)
#СОРТИРОВКА ТОВАРА

#Проверка что стоит сортировка по умолчанию
default_sorting=driver.find_element(By.CSS_SELECTOR,"[value='menu_order']")
default_sorting_checked=default_sorting.text
if default_sorting_checked=="Default sorting":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана другая сортировка")

#Изменение сортировки
sorting=driver.find_element(By.CSS_SELECTOR,"[value='price-desc']")
sorting.click()
time.sleep(3)
#Проверка, что сортировка по цене от большей к меньшей
high_to_low_sort=driver.find_element(By.CSS_SELECTOR,"[value='price-desc']")
high_to_low_sort_checked=high_to_low_sort.text
if high_to_low_sort_checked=="Sort by price: high to low":
    print("Выбрана сортировка цены от большей к меньшей")
else:
    print("Выбрана другая сортировка")

driver.quit()