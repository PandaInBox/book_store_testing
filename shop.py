import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

#book_bth=driver.find_element(By.XPATH,"//*[@id='content']//li[3]/a[1]/h3")
#book_bth.click()
#time.sleep(2)
#Проверка в тексте заголовка
#test_name_book=driver.find_element(By.CLASS_NAME,"entry-title")
#test_name_book_checked=test_name_book.text
#if test_name_book_checked=="HTML5 Forms":
#    print("Текст заголовка книги HTML5 Forms")
#else:
#    print("Текст заголовка книги не HTML5 Forms")

#КОЛЛИЧЕСТВО ТОВАРОВ

html_cat=driver.find_element(By.XPATH,"//*[@id='woocommerce_product_categories-2']//li[2]/a")
html_cat.click()
time.sleep(2)

items_count=driver.find_elements(By.CLASS_NAME,"woocommerce-LoopProduct-link")

if len(items_count) == 3:
 print("В списке товаров отображается 3 книги")
else:
 print("В списке товаров: " + str(len(items_count)))

driver.quit()