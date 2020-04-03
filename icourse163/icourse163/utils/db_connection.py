import logging
import MySQLdb as connector
from singleton_decorator import singleton
import traceback
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# FileHandler
file_handler = logging.FileHandler('result.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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
                logger.error('Faild to execute %s', query, exc_info=True)
                traceback.print_exc()
                sys.exit()
        except Exception:
            logger.error('Faild to execute %s', query, exc_info=True)
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
