import selectors
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.saucedemo.com')
driver.maximize_window()


driver.find_element_by_id('user-name').send_keys('standard_user')
import time 
time.sleep(1)
driver.find_element_by_id ('password').send_keys('secret_sauce')
time.sleep(1)
driver.find_element_by_id('login-button').click()
time.sleep(1)

driver.find_element_by_class_name('product_sort_container').click()
time.sleep(1)
    
select_element = driver.find_element(By.XPATH,'//select')
select_object = Select(select_element)
Select(select_element).select_by_value("lohi")
time.sleep(1)

add_to_cart_sauce_labs_onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
add_to_cart_sauce_labs_onesie.click()
time.sleep(1)

add_to_cart_test_allthethings_t_shi_ = driver.find_element(By.CSS_SELECTOR, "[id = 'add-to-cart-test.allthethings()-t-shirt-(red)']")
add_to_cart_test_allthethings_t_shi_.click()
time.sleep(1)

_2 = driver.find_element(By.XPATH, "//a[. = '2']")
_2.click()
time.sleep(1)
    
checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout.click()
time.sleep(1)
   
firstname = driver.find_element(By.CSS_SELECTOR, "#first-name")
firstname.click()
time.sleep(1)
    
firstname = driver.find_element(By.CSS_SELECTOR, "#first-name")
firstname.send_keys("Filomena")
time.sleep(1)
   
lastname = driver.find_element(By.CSS_SELECTOR, "#last-name")
lastname.click()
time.sleep(1)
 
lastname = driver.find_element(By.CSS_SELECTOR, "#last-name")
lastname.send_keys("Jonson")
time.sleep(1)

postalcode = driver.find_element(By.CSS_SELECTOR,"#postal-code")
postalcode.click()
time.sleep(1)

postalcode = driver.find_element(By.CSS_SELECTOR,"#postal-code")
postalcode.send_keys("01439001")
time.sleep(1)

_continue = driver.find_element(By.CSS_SELECTOR, "#continue")
_continue.click()
time.sleep(1)

driver.execute_script("window.scrollBy(0,332)")
time.sleep(1)

finish = driver.find_element(By.CSS_SELECTOR, "#finish")
finish.click()
time.sleep(1)
 
driver.execute_script("window.scrollBy(0,-332)")
