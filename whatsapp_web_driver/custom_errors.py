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
        
        
class NoContactFound(Exception):
    """
    Exception raised when contact is not found.
    Indicating that no such contact/group was present.
    """
    def __init__(self, message="Contact/Group not found."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nTry entering more accurate contact/Group detail as in Name or Number pre-existing in your contacts.'

class Already_Blocked(Exception):
    """
    Exception raised when contact is already blocked.
    Indicating that the current contact is blocked.
    """
    def __init__(self, message="Contact is blocked."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nTry entering a contact which is not blocked already.'

class NotContact(Exception):
    """
    Exception raised when contact is not provided.
    Indicating that the current tab is of group.
    """
    def __init__(self, message="Group is provided."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nTry entering a contact and not a group.'

class NotProvided(Exception):
    """
    Exception raised when contact does not provided online details.
    Indicating that the current contact might be absent.
    """
    def __init__(self, message="Cant provide online detail."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}\nTry entering a contact with presence of sharing online detail.'