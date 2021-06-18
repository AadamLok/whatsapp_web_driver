
from whatsapp_web_driver import WhatsappWebDriver, ChromeDriverNotWorking, MaxTimeOut, NoContactFound, ContactChat
import pytest
import time

def test_WWD_init_returns_error():
    with pytest.raises(ChromeDriverNotWorking):
        pytest.WWD = WhatsappWebDriver(chrome_driver=" ")

def test_WWD_start():
    try:
        pytest.WWD = WhatsappWebDriver()
    except MaxTimeOut:
        pytest.fail("Webpage took too much time to load, check your internet connection.")
    except:
        pytest.fail("Initiating WWD raises Exception.")

def test_is_logged_in():
    assert pytest.WWD.is_logged_in() == False, "Checking for web whatsapp not logged in"
    start_time = time.time()
    while not pytest.WWD.is_logged_in():
        if time.time()-start_time > 20:
            pytest.fail("Checking for web whatsapp logged in failed.")

def test_get_status_and_set_status():
    old_status = pytest.WWD.get_status()
    print(old_status)
    new_status = "😁text1😜text2😝"
    pytest.WWD.set_status(new_status)
    assert pytest.WWD.get_status() == new_status
    pytest.WWD.set_status(old_status)

def test_open_chat():
    pytest.test_contact = ContactChat(pytest.WWD, "9428556152")
    pytest.test_contact.open_chat()

def test_Wrong_contactDetail():
    with pytest.raises(NoContactFound):
        ContactChat(pytest.WWD, "adjsh").open_chat()

def test_isGroup():
    pytest.test_contact = ContactChat(pytest.WWD, "Memes and Weeb")
    if pytest.test_contact.is_group() == True:
        pytest.fail("Group")
    else :
        pytest.fail("Not Group")


def test_send_msg():
    for i in range(10):
        pytest.test_contact.send_message("Test msg "+str(i))

def test_close():
    assert pytest.WWD.close() == True, "Close the driver"