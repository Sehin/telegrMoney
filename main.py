import mysql.connector
from classes import DBWorker


def main():
    connection = mysql.connector.connect(user='root', password='Da!@#$%^&*()1',
                                         host='62.109.16.63',
                                         database='telegrMoney',
                                         auth_plugin='mysql_native_password')
    db = DBWorker.DBWorker(connection)

    pass


if __name__ == '__main__':
    main()
