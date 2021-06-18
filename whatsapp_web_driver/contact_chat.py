import time
from selenium.webdriver.common.action_chains import ActionChains
import win32clipboard
from whatsapp_web_driver.custom_errors import MaxTimeOut, WhatsappNotLoggedIn, NoContactFound
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class ContactChat:
    def __init__(self, WhatsappWebDriver, name_or_number):
        self.WWD = WhatsappWebDriver
        self.name_or_number = name_or_number
        self.current_message_id = ""
        self.title = None

    #Needs Work
    def open_chat(self):
        self.WWD.reload_page()
        
        if not self.WWD.is_logged_in():
            raise WhatsappNotLoggedIn()
        
        search_bar_XPATH = """//*[@id="side"]/div[1]/div/label"""
        all_results = """//*[@id="pane-side"]/div[1]/div/div"""
        msg_box_XPATH = """//*[@id="main"]/footer/div[1]/div[2]"""
        title_XPATH = """//*[@id="main"]/header/div[2]/div/div/span"""
        try:
            search_bar = WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH, search_bar_XPATH))
            )
            ActionChains(self.WWD.driver).move_to_element(search_bar).click().perform()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(self.name_or_number, win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()

            paste_action = ActionChains(self.WWD.driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
            paste_action.perform()

            time.sleep(5)

            all_results = self.WWD.driver.find_element(By.XPATH, all_results)
            all_results.find_elements(By.XPATH, """//*[@class="_2aBzC"]""")[-1].click()

            self.title = WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,title_XPATH))
            ).text if self.title == None else self.title

            WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,msg_box_XPATH))
            ).click()
        except TimeoutException:
            raise MaxTimeOut()
        except NoSuchElementException:
            raise NoContactFound()

        return True

    def send_message(self, message, tag_message_id=None):
        self.open_chat()

        title_XPATH = """//*[@id="main"]/header/div[2]/div/div/span"""
        
        try:
            while WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,title_XPATH))
            ).text != self.title:
                self.open_chat()
        
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(message, win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()

            paste_action = ActionChains(self.WWD.driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
            paste_action.perform()
            
            WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,"""//*[@id="main"]/footer/div[1]/div[3]/button"""))
            ).click()
            #TODO check previous msg you send is sent or not
        except TimeoutException:
            raise MaxTimeOut()

        return True

    def send_contact(self, name_or_number, index=0):
        self.open_chat()
        #TODO send contact to this chat,Aadam

    def send_document(self, path, tag_message_id=None):
        self.open_chat()
        #TODO copy the file in path
        # to clipboard and perfom paste
        # in the send box of chat
        # raise relevant exception
        # return True if succeful, Murtaza
        return False

    def get_new_msg_id(self):
        self.open_chat()
        #TODO get the message ID of the last
        # message in the chat, Aadam
        return None

    def set_current_msg_id(self, message_id):
        return None

    def get_next_message_id(self):
        return None

    def get_prev_message_id(self):
        return None

    def get_message_from_id(self, message_id):
        return None 

    def is_group(self):
        self.open_chat()

        title_XPATH = """//*[@id="main"]/header/div[2]/div/div/span"""

        try:
            while WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,title_XPATH))
            ).text != self.title:
                self.open_chat()
            
            title = self.WWD.driver.find_element(By.XPATH, title_XPATH).click()
            time.sleep(2)

            test1 = """/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[2]"""
            test = WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
               EC.visibility_of_element_located((By.XPATH,test1))
            ).text

            if test == "Group info":
                return True
            else:
                return False

        except TimeoutException:
            raise MaxTimeOut()
        
    def is_online(self):
        #Murtaza
        return None

    def get_profile_pic(self):
        return None

    def block_chat(self):
        #Murtaza
        return None

    def delete_chat(self):
        self.open_chat()

        title_XPATH = """//*[@id="main"]/header/div[2]/div/div/span"""

        try:
            while WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,title_XPATH))
            ).text != self.title:
                self.open_chat()
            time.sleep(1.5)

            list = """//*[@id="main"]/header/div[3]/div/div[2]/div/div"""
            WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,list))
            ).click()
            

            delete_btn = """//*[@id="app"]/div[1]/span[4]/div/ul/div/div/li[5]"""
            WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,delete_btn))
            ).click()

            confirm_del = """//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div"""
            WebDriverWait(self.WWD.driver, self.WWD.max_wait).until(
                EC.visibility_of_element_located((By.XPATH,confirm_del))
            ).click()


        except TimeoutException:
            raise MaxTimeOut()

    def delete_message(self, message_id, for_everyone=False):
        return None

    def message_info(self, message_id):
        return None

    def search_chat(self, to_search):
        return None