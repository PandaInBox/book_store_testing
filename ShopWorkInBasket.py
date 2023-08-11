import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

shop_bth = driver.find_element(By.ID, "menu-item-40")
shop_bth.click()
time.sleep(2)
# Скрол вниз на 300 пикселей
driver.execute_script("window.scrollBy(0,300);")
# добавление книг в корзину
one_book_add = driver.find_element(By.XPATH, "//*[@id='content']//li[4]/a[2]")
one_book_add.click()
time.sleep(1)
second_book_add = driver.find_element(By.XPATH, "//*[@id='content']//li[5]/a[2]")
second_book_add.click()
time.sleep(1)
# Переход в корзину
basket_bth = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
basket_bth.click()
time.sleep(2)
remove_bth = driver.find_element(By.XPATH, "//*[@id='page-34']//tr[1]/td[1]/a")
remove_bth.click()
time.sleep(2)
undo_bth = driver.find_element(By.CSS_SELECTOR, " div.woocommerce-message > a")
undo_bth.click()
time.sleep(2)
quntity = driver.find_element(By.XPATH, "//*[@id='page-34']//tr[1]/td[5]/div/input")
quntity.clear()
quntity.send_keys("3")
time.sleep(2)
update_basket = driver.find_element(By.NAME, "update_cart")
update_basket.click()
time.sleep(3)
#Проверка
quntity_text = driver.find_element(By.XPATH, "//*[@id='page-34']//tr[1]/td[5]/div/input").get_attribute("value")
print(quntity_text)
assert quntity_text == "3"
time.sleep(2)
apply_coupon_bth=driver.find_element(By.XPATH,"//*[@id='page-34']//tr[3]/td/div/input[2]")
apply_coupon_bth.click()
time.sleep(2)
#Проверка
coupon_code=driver.find_element(By.CLASS_NAME,"woocommerce-error")
coupon_code_text=coupon_code.text
assert coupon_code_text=="Please enter a coupon code."

driver.quit()