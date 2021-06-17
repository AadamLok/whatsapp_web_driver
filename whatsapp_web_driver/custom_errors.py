class ChromeDriverNotWorking(Exception):
    """
    Exception raised when driver passed in doesn't work and selimium throws error.
    """

    def __init__(self, place, message="Something is wrong with chrome driver."):
        self.message = message
        self.place = place
        super().__init__(self.message)

    def __str__(self):
        return f'Chrome driver passed in the {self.place} is not working.\nTry checking the path of chrome driver, or check in if your installed chrome version matches with driver version.'

class WhatsappNotLoggedIn(Exception):
    """
    Exception raised when web whatsapp is not logged in.
    """

    def __init__(self, message="Web Whatsapp not logged in."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nLog in to web whatsapp by scaning the barcode and then try again.'

class MaxTimeOut(Exception):
    """
    Exception raised when some element or page takes more time than
    max_time to load in. Indecating something is wrong with the Internet.
    """

    def __init__(self, message="Page took too much time to load."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nTry checking your Internet connection.'