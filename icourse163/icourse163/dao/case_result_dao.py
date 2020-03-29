from icourse163.utils.db_connection import DBConnection


class CaseResultDao(object):
    def __int__(self):
        pass

    def save(self, case_result):
        db = DBConnection()

        param = []
        param.append(case_result.test_id)
        param.append(case_result.answer_id)
        param.append(case_result.case_id)
        param.append(case_result.passs)
        param.append(case_result.result)
        param.append(case_result.score)
        param.append(case_result.tips)
        param.append(case_result.used_cpu_time)
        param.append(case_result.used_memory)

        query = "INSERT INTO case_result (testId, answerId, caseId, passs, result, score, tips, usedCpuTime, usedMemory) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
