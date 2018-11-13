from classes.dao.Repository import Repository
from classes.domain import Category


class CategoryRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, "Category")

    def getById(self, id: int) -> Category:
        return super().getById(id)

    def save(self, category: Category) -> None:
        sql = "INSERT INTO `{}` (`chat_id`, `name`) VALUES ('{}', '{}');".format(
            self.tableName, category.id, category.name)
        self.executeSql(sql)

    def getCategoriesByChatId(self, chat_id) -> Category:
        sql = "SELECT ctg.* FROM " \
              "CategoryInUser ciu, User usr, Category ctg " \
              "where ciu.id_category = ctg.id and " \
              "ciu.id_user = usr.id and " \
              "usr.id = (select id from User where chat_id = {})" \
            .format(chat_id)
        return self.selectSql(sql)