class DBWorker():

    def __init__(self, connection):
        self.connection = connection
        pass

    def insertSql(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def selectSql(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def saveUser(self, chat_id, name, balance):
        sql = "INSERT INTO `telegrMoney`.`User` (`chat_id`, `name`, `balance`) VALUES ('{}', '{}', '{}');".format(chat_id, name, balance)
        self.insertSql(sql)

    def saveMoney(self, id_cat, count, date):
        sql = "INSERT INTO `telegrMoney`.`Money` (`count`, `date`, `id_cat`) VALUES ('{}', '{}', '{}');".format(count, date, id_cat)
        self.insertSql(sql)

    def saveCategory(self, name, hash):
        sql = "INSERT INTO `telegrMoney`.`Category` (`name`, `hash`) VALUES ('{}', '{}');".format(name, hash)
        self.insertSql(sql)

    def saveCategoryInUser(self, id_cat, id_user):
        sql = "INSERT INTO `telegrMoney`.`CategoryInUser` (`id_category`, `id_user`) VALUES ('{}', '{}');".format(id_cat, id_user)
        self.insertSql(sql)

    # Category name and hash
    def getCategories(self, chat_id):
        sql = "SELECT ctg.name, ctg.hash FROM " \
              "telegrMoney.CategoryInUser ciu, telegrMoney.User usr, telegrMoney.Category ctg " \
              "where ciu.id_category = ctg.id and " \
              "ciu.id_user = usr.id and " \
              "usr.id = (select id from telegrMoney.User where chat_id = {})"\
            .format(chat_id)
        return self.selectSql(sql)

    def getUser(self, chat_id):
        pass
    #... something else :-)