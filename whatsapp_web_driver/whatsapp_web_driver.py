from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .custom_errors import ChromeDriverNotWorking, WhatsappNotLoggedIn

class WhatsappWebDriver():
    def __init__(self, chrome_driver):
        try:
            self.driver = webdriver.Chrome(executable_path=chrome_driver)
            self.start()
        except:
            raise ChromeDriverNotWorking(place="parameter 'chrome_driver' of whatsapp_web_driver class")
    
    def start(self):
        self.driver.get("https://web.whatsapp.com/")
        return self.check_logged_in()

    def check_logged_in(self):
        #TODO check logged in or not
        #return true if logged in else
        #raise WhatsappNotLoggedIn error
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

    