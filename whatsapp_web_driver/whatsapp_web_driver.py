from posixpath import expanduser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

from .custom_errors import ChromeDriverNotWorking, WhatsappNotLoggedIn, MaxTimeOut
from .custom_wait import presence_of_any_one_element_located

class WhatsappWebDriver():
    def __init__(self, chrome_driver="", max_wait=10):
        dirname = os.path.dirname(__file__)
        chrome_driver = os.path.join(dirname, 'chromedriver.exe') if chrome_driver == "" else chrome_driver
        try:
            self.driver = webdriver.Chrome(executable_path=chrome_driver)
        except:
            raise ChromeDriverNotWorking(place="parameter 'chrome_driver' of whatsapp_web_driver class")
        self.max_wait = max_wait
        self.start()
    
    def start(self):
        self.driver.get("https://web.whatsapp.com/")
        try:
            WebDriverWait(self.driver, self.max_wait).until(
                presence_of_any_one_element_located(
                    (By.XPATH,"""//*[@id="side"]/div[1]/div"""),
                    (By.XPATH,"""//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas""")
                )
            )
        except TimeoutException:
            raise MaxTimeOut()

    def is_logged_in(self):
        try:
            self.driver.find_element(By.XPATH, """//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas""")
            return False
        except NoSuchElementException:
            return True

    def change_status(self, new_status="Whatsapp being controlled by WhatsappWebDriver."):
        #TODO check if whatsapp is logged in
        #then change the status
        #raise relevant errors
        # in the end retun True
        return True

    def get_current_status(self):
        #TODO get the current status
        # and retun it
        # raise relevant errors
        return None

    def close(self):
        self.driver.quit()
        return True