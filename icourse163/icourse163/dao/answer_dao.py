from icourse163.utils.db_connection import DBConnection


class AnswerDao(object):
    def __int__(self):
        pass

    def save(self, answer):
        db = DBConnection()

        param = []
        param.append(answer.id)
        param.append(answer.aid)
        param.append(answer.answerer_id)
        param.append(answer.deadline)
        param.append(answer.effect_status)
        param.append(answer.exam_id)
        param.append(answer.final_score)
        param.append(answer.name)
        param.append(answer.nickname)
        param.append(answer.objective_score)
        param.append(answer.score)
        param.append(answer.score_pub_status)
        param.append(answer.show_score)
        param.append(answer.subjective_score)
        param.append(answer.submit_time)
        param.append(answer.test_id)
        param.append(answer.tid)
        param.append(answer.total_score)
        param.append(answer.type)

        query = "INSERT INTO answer (id, aid, answererId, deadline, effectStatus, examId, finalScore, name, nickname, objectiveScore, score, scorePubStatus, showScore, subjectiveScore, submitTime, testId, tid, totalScore, type) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18});".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
