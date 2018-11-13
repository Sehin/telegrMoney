class Repository():
    def __init__(self, connection, tableName):
        self.connection = connection
        self.tableName = tableName
        pass

    def executeSql(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def selectSql(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def getById(self, id: int):
        sql = "SELECT * FROM '{}' where id = {}".format(self.tableName, id)
        return self.selectSql(sql)

    def selectLastId(self) -> int:
        sql = "SELECT max(id) FROM '{}'".format(self.tableName)
        return self.selectSql(sql)
