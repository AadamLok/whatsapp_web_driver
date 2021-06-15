from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from .custom_errors import ChromeDriverNotWorking, WhatsappNotLoggedIn, MaxTimeOut

class WhatsappWebDriver():
    def __init__(self, chrome_driver="", max_wait=10):
        try:
            dirname = os.path.dirname(__file__)
            chrome_driver = os.path.join(dirname, 'chromedriver.exe') if chrome_driver == "" else chrome_driver
            self.driver = webdriver.Chrome(executable_path=chrome_driver)
            self.max_wait = max_wait
            self.start()
        except:
            raise ChromeDriverNotWorking(place="parameter 'chrome_driver' of whatsapp_web_driver class")
    
    def start(self):
        self.driver.get("https://web.whatsapp.com/")
        start_time = time.time()
        page_state = ""
        while page_state != "complete":
            page_state = self.driver.execute_script('return document.readyState;')
            if time.time()-start_time > self.max_wait:
                raise MaxTimeOut()
        return self.is_logged_in()

    def is_logged_in(self):
        #TODO check logged in or not
        #return true if logged in else
        #raise WhatsappNotLoggedIn error
        return False

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