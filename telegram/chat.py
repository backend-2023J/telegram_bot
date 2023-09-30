class Chat:
    def __init__(self, chat) -> None:
        self.id = chat['id']
        self.first_name = chat['first_name']
        self.username = chat['username']
        self.last_name = chat['last_name']