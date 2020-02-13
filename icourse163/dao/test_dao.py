from icourse163.utils.db_connection import DBConnection
from icourse163.test import Test


class TestDao(object):
    def __int__(self):
        pass

    def save(self, test):
        db = DBConnection()

        param = []
        param.append(test.test_id)
        param.append(test.description)
        param.append(test.deadline)
        param.append(test.exam_id)
        param.append(test.chapter_id)
        param.append(test.gmt_create)
        param.append(test.gmt_modified)
        param.append(test.name)
        param.append(test.release_time)
        param.append(test.term_id)
        param.append(test.total_score)
        param.append(test.trytime)
        param.append(test.type)

        query = "INSERT INTO test (testId, description, deadline, examId, chapterId, gmtCreate, gmtModified, name, releaseTime, termId, totalScore, trytime, type) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12});".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
