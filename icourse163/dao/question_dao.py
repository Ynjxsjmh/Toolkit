from icourse163.utils.db_connection import DBConnection


class QuestionDao(object):
    def __int__(self):
        pass

    def save(self, question):
        db = DBConnection()

        param = []
        param.append(question.id)
        param.append(question.allow_upload)
        param.append(question.description)
        param.append(question.gmt_create)
        param.append(question.gmt_modified)
        param.append(question.oj_mem_limit)
        param.append(question.oj_need_input)
        param.append(question.oj_supported_language)
        param.append(question.oj_time_limit)
        param.append(question.oj_try_time)
        param.append(question.options)
        param.append(question.options_detail)
        param.append(question.plain_text_title)
        param.append(question.position)
        param.append(question.score)
        param.append(question.test_id)
        param.append(question.title)
        param.append(question.type)

        query = "INSERT INTO icourse163.question (id, allowUpload, description, gmtCreate, gmtModified, ojMemLimit, ojNeedInput, ojSupportedLanguage, ojTimeLimit, ojTryTime, options, optionsDetail, plainTextTitle, position, score, testId, title, type) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17});".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
