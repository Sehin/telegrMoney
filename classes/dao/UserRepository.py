from classes.dao.Repository import Repository
from classes.domain import User


class UserRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, "User")

    def getById(self, id: int) -> User:
        return super().getById(id)

    def saveUser(self, user: User):
        sql = "INSERT INTO `{}` (`chat_id`, `name`, `balance`) VALUES ('{}', '{}', '{}');".format(
            self.tableName,
            user.chat_id, user.name, user.balance)
        self.executeSql(sql)

    def getUserByChatId(self, chat_id: int):
        sql = "SELECT * FROM '{}' WHERE chat_id = {}".format(self.tableName, chat_id)
        self.selectSql(sql)
