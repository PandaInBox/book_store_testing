import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

shop_bth = driver.find_element(By.ID, "menu-item-40")
shop_bth.click()
time.sleep(2)
# Скрол вниз на 300 пикселей
driver.execute_script("window.scrollBy(0,300);")
one_book_add = driver.find_element(By.XPATH, "//*[@id='content']//li[4]/a[2]")
one_book_add.click()
time.sleep(1)
# Корзина
basket_bth = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
basket_bth.click()
time.sleep(2)
# Проверка явного ожидания
proceed_to_checkout_checked = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//*[@id='page-34']//div/a"), "PROCEED TO CHECKOUT")
)
proceed_to_checkout_bth = driver.find_element(
    By.XPATH, "//*[@id='page-34']//div/a")
proceed_to_checkout_bth.click()
time.sleep(2)
# явное ожидание для имени и заполнение обязательных полей
first_name_cheked = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//*[@id='billing_first_name_field']/label"), "First Name *")
)
first_name = driver.find_element(By.CSS_SELECTOR, "#billing_first_name")
first_name.send_keys("Max")
last_name = driver.find_element(By.CSS_SELECTOR, "#billing_last_name")
last_name.send_keys("Volwo")
email = driver.find_element(By.CSS_SELECTOR, "#billing_email")
email.send_keys("swat1155@mail.ru")
phone = driver.find_element(By.XPATH, "//*[@id='billing_phone']")
phone.send_keys("+79216542760")

country = driver.find_element(By.CSS_SELECTOR, "#s2id_billing_country > a")
country.click()
country_input = driver.find_element(By.CSS_SELECTOR, "#s2id_autogen1_search")
country_input.send_keys("Russia")
time.sleep(1)
country_name = driver.find_element(By.CSS_SELECTOR, "#select2-results-1 > li")
country_name.click()
time.sleep(1)

address = driver.find_element(By.XPATH, "//*[@id='billing_address_1']")
address.send_keys("Politruca Pacechnika")
city = driver.find_element(By.XPATH, "//*[@id='billing_city']")
city.send_keys("New York")
state = driver.find_element(By.XPATH, "//*[@id='billing_state']")
state.send_keys("New York")
postcode = driver.find_element(By.XPATH, "//*[@id='billing_postcode']")
postcode.send_keys("2045")
time.sleep(2)
# Скролл вниз
driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)

check_payments = driver.find_element(By.CSS_SELECTOR, "#payment_method_cheque")
check_payments.click()

place_order = driver.find_element(By.CSS_SELECTOR, "#place_order")
place_order.click()
# Явное ожидание
text_under_place = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
check_paymants = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, " tr:nth-child(3) > td"), "Check Payments")
)

driver.quit()
