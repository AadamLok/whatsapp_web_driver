from whatsapp_web_driver.custom_errors import MaxTimeOut
from whatsapp_web_driver import WhatsappWebDriver, ChromeDriverNotWorking, MaxTimeOut
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

def test_close():
    assert pytest.WWD.close() == True, "Close the driver"