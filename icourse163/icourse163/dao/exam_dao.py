from icourse163.utils.db_connection import DBConnection


class ExamDao(object):
    def __int__(self):
        pass

    def save(self, exam):
        db = DBConnection()

        param = []
        param.append(exam.id)
        param.append(exam.avg_score)
        param.append(exam.bonus_score)
        param.append(exam.content_type)
        param.append(exam.deadline)
        param.append(exam.description)
        param.append(exam.draft_status)
        param.append(exam.gmt_create)
        param.append(exam.gmt_modified)
        param.append(exam.judge_type)
        param.append(exam.name)
        param.append(exam.object_test_id)
        param.append(exam.release_time)
        param.append(exam.subjective_score)
        param.append(exam.score_pub_status)
        param.append(exam.score_release_time)
        param.append(exam.subject_test_id)
        param.append(exam.sumit_test_count)
        param.append(exam.task_status)
        param.append(exam.term_id)
        param.append(exam.total_score)
        param.append(exam.user_score)

        query = "INSERT INTO `icourse163`.`exam` (`id`, `avgScore`, `bonusScore`, `contentType`, `deadline`, `description`, `draftStatus`, `gmtCreate`, `gmtModified`, `judgeType`, `name`, `objectTestId`, `releaseTime`, `scorePubStatus`, `scoreReleaseTime`, `subjectTestId`, `submitTestCount`, `taskStatus`, `termId`, `totalScore`, `userScore`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}');"

        result = db.execute_query(query)
        db.commit()

        return result
