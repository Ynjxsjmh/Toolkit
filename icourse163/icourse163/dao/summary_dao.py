from icourse163.utils.db_connection import DBConnection


class SummaryDao(object):
    def __int__(self):
        pass

    def save(self, summary):
        db = DBConnection()

        param = []
        param.append(summary.summary_id)
        param.append(summary.term_id)
        param.append(summary.member_id)
        param.append(summary.test_score)
        param.append(summary.assignment_score)
        param.append(summary.exam_score)
        param.append(summary.discuss_score)
        param.append(summary.reply_count)
        param.append(summary.vote_count)
        param.append(summary.outside_score)
        param.append(summary.total_score)
        param.append(summary.bonus_score)
        param.append(summary.total_score_with_bonus)
        param.append(summary.cert_type_now)
        param.append(summary.nick_name)
        param.append(summary.real_name)
        param.append(summary.student_number)
        param.append(summary.group_id)
        param.append(summary.group_name)
        param.append(summary.school_name)
        param.append(summary.departments)
        param.append(summary.professional)
        param.append(summary.clazz)
        param.append(summary.comment)
        param.append(summary.level)
        param.append(summary.final_score)

        query = "INSERT INTO summary (summaryId, termId, memberId, testScore, assignmentScore, examScore, discussScore, replyCount, voteCount, outsideScore, totalScore, bonusScore, totalScoreWithBonus, certTypeNow, nickName, realName, studentNumber, groupId, groupName, schoolName, departments, professional, clazz, comment, level, finalScore) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result

    def search_all(self):
        db = DBConnection()

        query = "select * from summary;"
        result = db.execute_query(query)

        return result

    def search_by_term_id(self, term_id):
        db = DBConnection()

        query = "SELECT * from summary where termId = {}".format(term_id)
        result = db.execute_query(query)

        return result
