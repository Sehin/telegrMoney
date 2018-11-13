class User():
    def __init__(self, id, chatId, name, balance) -> None:
        super.__init__(id)
        self.chatId = chatId
        self.name = name
        self.balance = balance
