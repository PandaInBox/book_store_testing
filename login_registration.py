import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

#регистрация аккаунта
account_bth=driver.find_element(By.ID,"menu-item-50")
account_bth.click()
time.sleep(3)
register_email=driver.find_element(By.ID,"reg_email")
register_email.send_keys("swat1155@mail.ru")
register_password=driver.find_element(By.ID,"reg_password")
register_password.send_keys("Grower1527_swen")

register_bth=driver.find_element(By.CSS_SELECTOR,"p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
register_bth.click()
time.sleep(3)

#Вход в аккаунт
driver.get("https://practice.automationtesting.in/")

account_bth=driver.find_element(By.ID,"menu-item-50")
account_bth.click()
time.sleep(3)
login_email=driver.find_element(By.ID,"username")
login_email.send_keys("swat1155@mail.ru")
login_password=driver.find_element(By.ID,"password")
login_password.send_keys("Grower1527_swen")

login_bth=driver.find_element(By.NAME,"login")
login_bth.click()
time.sleep(3)
logout=driver.find_element(By.XPATH,"//*[@id='page-36']//ul/li[6]/a")
logout_checked=logout.get_attribute("checked")
print(logout_checked)
if logout_checked is not None:
    print("На странице есть элемент logout")
else:
    print("На странице нет элемента logout")
driver.quit()