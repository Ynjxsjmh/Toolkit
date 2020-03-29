from icourse163.utils.db_connection import DBConnection


class QuestionSubmitRecordDao(object):
    def __int__(self):
        pass

    def save(self, question_submit_record):
        db = DBConnection()

        param = []
        param.append(question_submit_record.test_id)
        param.append(question_submit_record.test_answerform_id)
        param.append(question_submit_record.question_id)
        param.append(question_submit_record.user_id)
        param.append(question_submit_record.is_max_score)
        param.append(question_submit_record.score)
        param.append(question_submit_record.oj_submit_time)
        param.append(question_submit_record.status)

        query = "INSERT INTO question_submit_record (testId, answerId, questionId, userId, isMaxScore, score, ojSubmitTime, status) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
