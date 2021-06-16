from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import win32clipboard

from .custom_errors import ChromeDriverNotWorking, WhatsappNotLoggedIn, MaxTimeOut
from .custom_wait import presence_of_any_one_element_located, element_has_some_text

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

    def reload_page(self):
        self.driver.get("https://web.whatsapp.com/")

    def open_profile_page(self):
        self.reload_page()
        
        if not self.is_logged_in():
            raise WhatsappNotLoggedIn()

        side_page_profile_pic_element = None
        side_page_profile_pic_element_XPATH = """//*[@id="side"]/header/div[1]/div/img"""
        try:
            side_page_profile_pic_element = WebDriverWait(self.driver, self.max_wait).until(
                EC.element_to_be_clickable((By.XPATH,side_page_profile_pic_element_XPATH))
            )
        except TimeoutException:
            raise MaxTimeOut()
        
        side_page_profile_pic_element.click()

    def set_status(self, new_status="Whatsapp being controlled by WhatsappWebDriver."):
        self.open_profile_page()
        
        edit_status_element = None
        edit_status_element_XPATH = """//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4]/div[2]/div[1]/span[2]/div/span"""
        done_element = None
        done_XPATH = """//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4]/div[2]/div[1]/span[2]/div/span"""
        try:
            edit_status_element = WebDriverWait(self.driver, self.max_wait).until(
                EC.element_to_be_clickable((By.XPATH,edit_status_element_XPATH))
            )
            edit_status_element.click()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(new_status, win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()

            action = ActionChains(self.driver)
            action.key_down(Keys.SHIFT)
            for i in range(140):
                action.send_keys(Keys.LEFT)
            action.key_up(Keys.SHIFT).send_keys(Keys.DELETE)
            action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

            done_element = WebDriverWait(self.driver, self.max_wait).until(
                EC.element_to_be_clickable((By.XPATH, done_XPATH))
            )
            done_element.click()
        except TimeoutException:
            raise MaxTimeOut()
        
        return True
    
    def get_status(self):
        self.open_profile_page()
        
        status_element_XPATH = """//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4]/div[2]/div[1]/div/div[2]"""
        status_edit_element = None
        status_edit_element_XPATH = """//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[4]/div[2]/div[1]/span[2]/div/span"""
        try:
            WebDriverWait(self.driver, self.max_wait).until(
                element_has_some_text((By.XPATH,status_element_XPATH))
            )
            status_edit_element = WebDriverWait(self.driver, self.max_wait).until(
                EC.element_to_be_clickable((By.XPATH, status_edit_element_XPATH))
            )
            status_edit_element.click()
        except TimeoutException:
            raise MaxTimeOut()

        action = ActionChains(self.driver).key_down(Keys.SHIFT)
        for i in range(140):
            action.send_keys(Keys.LEFT)
        action.key_up(Keys.SHIFT).key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()

        win32clipboard.OpenClipboard()
        status = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()

        return status

    def close(self):
        self.driver.quit()
        return True