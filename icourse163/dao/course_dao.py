from icourse163.utils.db_connection import DBConnection
from icourse163.course import Course


class CourseDao(object):
    def __init__(self):
        pass

    def save(self, course):
        db = DBConnection()

        param = []
        param.append(course.course_id)
        param.append(course.course_type)
        param.append(course.current_term_chargeable)
        param.append(course.current_term_id)
        param.append(course.gmt_create)
        param.append(course.img_url)
        param.append(course.course_name)
        param.append(course.school_id)
        param.append(course.course_short_name)

        query = "INSERT INTO course (courseId, courseType, currentTermChargeable, currentTermId, gmtCreate, imgUrl, courseName, schoolId, courseShortName) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8});".format(*param)

        result = db.execute_query(query)

        db.commit()

        return result
