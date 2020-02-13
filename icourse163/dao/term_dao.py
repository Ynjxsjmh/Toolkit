from icourse163.utils.db_connection import DBConnection
from icourse163.term import Term


class TermDao(object):
    def __int__(self):
        pass

    def save(self, term):
        db = DBConnection()

        param = []
        param.append(term.term_id)
        param.append(term.achievement_status)
        param.append(term.course_id)
        param.append(term.end_time)
        param.append(term.start_time)
        param.append(term.enroll_count)
        param.append(term.lessons_count)
        param.append(term.school_id)

        query = "INSERT INTO term (termId, achievementStatus, courseId, endTime, startTime, enrollCount, lessonsCount, schoolId) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7});".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result
