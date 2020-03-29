from icourse163.utils.db_connection import DBConnection


class AnswerDetailDao(object):
    def __int__(self):
        pass

    def save(self, answer_detail):
        db = DBConnection()

        param = []
        param.append(answer_detail.answer_id)
        param.append(answer_detail.test_id)
        param.append(answer_detail.qid)
        param.append(answer_detail.answer_times)
        param.append(answer_detail.content)
        param.append(answer_detail.correct)
        param.append(answer_detail.correct_count)
        param.append(answer_detail.last_answer_id)
        param.append(answer_detail.max_score_answer_id)
        param.append(answer_detail.q_correct_count)
        param.append(answer_detail.score)
        param.append(answer_detail.type)

        query = "INSERT INTO answer_detail (answerId, testId, qid, answerTimes, content, correct, correctCount, lastAnswerId, maxScoreAnswerId, qCorrectCount, score, type) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
