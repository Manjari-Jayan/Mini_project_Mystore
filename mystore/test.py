# from datetime import datetime
# from lib2to3.pgen2 import driver
# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/'

#     def tearDown(self):
#         self.driver.quit()
        
#     def test_01_login_page(self):
#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(1)

#         coloncare=driver.find_element(By.ID,'loginid')
#         coloncare.click()
#         time.sleep(2)

#         coloncare=driver.find_element(By.ID,'username')
#         coloncare.send_keys("ishta@gmail.com")
#         time.sleep(2)
        
#         coloncare=driver.find_element(By.ID,'password')
#         coloncare.send_keys("Ishta@1234")
#         time.sleep(2)

#         coloncare=driver.find_element(By.ID,'submit')
#         coloncare.click()
#         # time.sleep(2)

#         coloncare=driver.find_element(By.ID,'submit')
#         coloncare.click()
#         time.sleep(2)

#         # driver.execute_script("window.scrollBy(0, 1500);")
#         # time.sleep(2)

#         coloncare = driver.find_element(By.CSS_SELECTOR, 'a.nav-link > span > i.fa.fa-heart')
#         coloncare.click()
#         time.sleep(2)



from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Hosttest(TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.driver.quit()


    def test_02_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(2)

        theme=driver.find_element(By.CSS_SELECTOR,"a.nav-link#loginid") 
        theme.click()
        elem = driver.find_element(By.NAME, "username")
        elem.send_keys("ishta@gmail.com")
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys("Ishta@1234")
        # time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']#submit.btn.btn-success")
        submit_button.click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 2000);")
        time.sleep(2)
        browse=driver.find_element(By.CSS_SELECTOR,"a.nav-link > i.fa.fa-heart")
        browse.click()
        time.sleep(2)
        
        driver.execute_script("window.scrollBy(0, 500);")
        browse=driver.find_element(By.CSS_SELECTOR,"a.img-prod")
        browse.click()
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        browse=driver.find_element(By.CSS_SELECTOR,"button.add-to-cart-button[name='buy_now']")
        browse.click()
        time.sleep(5)

if __name__ == '_main_':
    import unittest
    unittest.main()
        