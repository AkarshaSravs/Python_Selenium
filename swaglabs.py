from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.ID,'password').send_keys("secret_sauce")
driver.find_element(By.ID,'login-button').click()
driver.find_element(By.XPATH, '//div[@class="inventory_item_name "and text()="Test.allTheThings() T-Shirt (Red)"]').click()
driver.find_element(By.ID, 'add-to-cart').click()
driver.find_element(By.ID, 'back-to-products').click()
driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
driver.find_element(By.ID, 'checkout').click()
driver.find_element(By.ID, 'first-name').send_keys("Lakshmi")
driver.find_element(By.ID, 'last-name').send_keys("Narayan")
driver.find_element(By.ID, 'postal-code').send_keys("352473")
driver.find_element(By.ID, 'continue').click()
final_message= driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div').text
print(final_message)
driver.find_element(By.ID, 'finish').click()
driver.close()