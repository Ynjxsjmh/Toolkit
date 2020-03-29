import MySQLdb as connector
from singleton_decorator import singleton
import traceback
import sys


@singleton
class DBConnection(object):
    # __metaclass__  = Singleton
    # https://stackoverflow.com/questions/13508079
    # https://medium.com/better-programming/singleton-in-python-5eaa66618e3d

    def __init__(self):
        print("Connecting database...")
        with open("dbconfig.txt", "r") as f:
            text = f.readline()

        config = text[:-1].split(",")
        self.dbConnection = connector.Connect(host=config[0], user=config[1],
                                              passwd=config[2], db=config[3],
                                              charset='utf8')

        self.dbCursor = self.dbConnection.cursor()
        print("Connected")

    def get_connection(self):
        return self.dbConnection

    def execute_query(self, query):
        result = None

        try:
            self.dbCursor.execute(query)
            result = self.dbCursor.fetchall()
        except connector.IntegrityError as e:
            if "Duplicate entry" in str(e) and "PRIMARY" in str(e):
                pass
            else:
                traceback.print_exc()
                sys.exit()
        except Exception:
            print(sys.exc_info()[0])
            traceback.print_exc()
            sys.exit()

        return result

    def commit(self):
        self.dbConnection.commit()

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()


if __name__ == '__main__':
    db = DBConnection()
    query = "select * from term where termId = 20"
    result = db.execute_query(query)
