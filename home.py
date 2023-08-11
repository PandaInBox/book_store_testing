import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

add_to_basket_bth=driver.find_element(By.XPATH,"//*[@id='text-22-sub_row_1-0-2-0-0']//h3")
add_to_basket_bth.click()
time.sleep(3)
reviews_bth=driver.find_element(By.CLASS_NAME,"reviews_tab")
reviews_bth.click()

rating_star_bth=driver.find_element(By.CLASS_NAME,"star-5")
rating_star_bth.click()
review_text=driver.find_element(By.ID,"comment")
review_text.send_keys("Nice book!")
name_text=driver.find_element(By.ID,"author")
name_text.send_keys("Joe Golberg")
email_text=driver.find_element(By.ID,"email")
email_text.send_keys("PandaGold@gmail.com")

submit_bth=driver.find_element(By.ID,"submit")
submit_bth.click()
time.sleep(3)
driver.quit()
