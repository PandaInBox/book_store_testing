import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()

#Обновление вебдрайвера для хром
# #from selenium.webdriver.chrome.service import Service
#service = Service()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service, options=options)
#или это:
#service = Service(executable_path='./chromedriver.exe')
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service, options=options)



driver.get("https://practice.automationtesting.in/")

shop_bth=driver.find_element(By.ID,"menu-item-40")
shop_bth.click()
time.sleep(2)
book_add_to_basket=driver.find_element(By.XPATH,"//*[@id='content']/ul/li[4]/a[2]")
book_add_to_basket.click()
time.sleep(1)
#Проверка корзины
item=driver.find_element(By.CSS_SELECTOR,"a > span.cartcontents")
item_text=item.text
assert item_text=="1 Item"
price=driver.find_element(By.XPATH,"//*[@id='wpmenucartli']/a/span[2]")
price_text=price.text
assert price_text=="₹180.00"

basket_open=driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
basket_open.click()
#явное ожидание
subtotal=WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.XPATH,"//*[@id='page-34']//div/table/tbody/tr[1]/td/span"),"₹180.00")
)
time.sleep(3)
total=WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.XPATH,"//*[@id='page-34']//tr[3]/td/strong/span"),"₹183.60")
)

driver.quit()