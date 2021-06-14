class ContactChat:
    def __init__(self, WhatsappWebDriver, name_or_number, index=0):
        self.WWD = WhatsappWebDriver
        self.name_or_number = name_or_number
        self.index = 0
        self.current_message_id = ""

    def open_chat(self):
        #TODO open chat with info
        # in self, raise apropriate
        # exceptions, return true if
        # successful
        return False

    def send_message(self, message, tag_message_id=None):
        self.open_chat()
        #TODO send msg specified
        #raise apropriate erros
        #return True if successful
        return False

    def send_contact(self, name_or_number, index=0):
        self.open_chat()
        #TODO send contact to this chat

    def send_document(self, path, tag_message_id=None):
        self.open_chat()
        #TODO copy the file in path
        # to clipboard and perfom paste
        # in the send box of chat
        # raise relevant exception
        # return True if succeful
        return False

    def get_new_msg_id(self):
        self.open_chat()
        #TODO get the message ID of the last
        # message in the chat
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
        return None

    def is_online(self):
        return None

    def get_profile_pic(self):
        return None

    def block_chat(self):
        return None

    def delete_chat(self):
        return None

    def delete_message(self, message_id, for_everyone=False):
        return None

    def message_info(self, message_id):
        return None

    def search_chat(self, to_search):
        return None