import MySQLdb as connector
from singleton_decorator import singleton


@singleton
class DBConnection(object):
    # __metaclass__  = Singleton
    # https://stackoverflow.com/questions/13508079
    # https://medium.com/better-programming/singleton-in-python-5eaa66618e3d

    def __init__(self):
        with open("../dbconfig.txt", "r") as f:
            text = f.readline()

        config = text[:-1].split(",")
        self.dbConnection = connector.Connect(host=config[0], user=config[1],
                                              passwd=config[2], db=config[3])

        self.dbCursor = self.dbConnection.cursor()

    def get_connection(self):
        return self.dbConnection

    def execute_query(self, query):
        self.dbCursor.execute(query)

        result = self.dbCursor.fetchall()

        return result

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()


if __name__ == '__main__':
    db = DBConnection()
    query = "select * from term where termId = 20"
    result = db.execute_query(query)
