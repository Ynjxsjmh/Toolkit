from icourse163.utils.db_connection import DBConnection


class SummaryDao(object):
    def __int__(self):
        pass

    def save(self, summary):
        db = DBConnection()

        param = []
        param.append(summary.id)
        param.append(summary.aid)
        param.append(summary.summaryer_id)
        param.append(summary.deadline)
        param.append(summary.effect_status)
        param.append(summary.exam_id)
        param.append(summary.final_score)
        param.append(summary.name)
        param.append(summary.nickname)
        param.append(summary.objective_score)
        param.append(summary.score)
        param.append(summary.score_pub_status)
        param.append(summary.show_score)
        param.append(summary.subjective_score)
        param.append(summary.submit_time)
        param.append(summary.test_id)
        param.append(summary.tid)
        param.append(summary.total_score)
        param.append(summary.type)

        query = "INSERT INTO summary (summaryId, termId, memberId, testScore, assignmentScore, examScore, discussScore, replyCount, voteCount, outsideScore, totalScore, bonusScore, totalScoreWithBonus, certTypeNow, nickName, realName, studentNumber, groupId, groupName, schoolName, departments, professional, clazz, comment, level, finalScore) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26});".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
