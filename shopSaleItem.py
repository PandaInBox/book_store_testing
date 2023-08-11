import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/shop/")
#Книга Android Quick Start Guide
book_open=driver.find_element(By.XPATH,"//*[@id='content']//li[1]/a[1]")
book_open.click()
time.sleep(2)
#Проверка старой и новой цены
old_price=driver.find_element(By.XPATH,"//*[@id='product-169']//p/del/span")
old_price_text=old_price.text
assert old_price_text=="₹600.00"
new_price=driver.find_element(By.XPATH,"//*[@id='product-169']//div/p/ins/span")
new_price_text=new_price.text
assert new_price_text=="₹450.00"

#Открытие изображения и реализация явного ожидания
img=WebDriverWait(driver,10).until(
    EC.invisibility_of_element_located((By.ID,"fullResImage"))
)
open_img=driver.find_element(By.XPATH,"//*[@id='product-169']//a/img")
open_img.click()
time.sleep(2)
#Закрытие изображения через крестик и явное ожидание
cross=WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME,"pp_close"),"Close")
)
cross_bth=driver.find_element(By.CLASS_NAME,"pp_close")
cross_bth.click()
time.sleep(2)

driver.quit()