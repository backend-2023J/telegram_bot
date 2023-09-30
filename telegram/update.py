from .message import Message

class Update:
    def __init__(self,update:dict):
        self.update_id = update['update_id']
        self.message = Message(update['message'])