from icourse163.utils.db_connection import DBConnection


class CourseDao(object):
    def __init__(self):
        pass

    def save(self, course):
        db = DBConnection()

        param = []
        param.append(course.id)
        param.append(course.course_type)
        param.append(course.current_term_chargeable)
        param.append(course.current_term_id)
        param.append(course.gmt_create)
        param.append(course.img_url)
        param.append(course.name)
        param.append(course.school_id)
        param.append(course.short_name)

        query = "INSERT INTO course (id, courseType, currentTermChargeable, currentTermId, gmtCreate, imgUrl, name, schoolId, shortName) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, '{6}', {7}, {8});".format(*param)

        result = db.execute_query(query)

        db.commit()

        return result

    def search_all(self):
        db = DBConnection()
        query = "SELECT * from course"
        result = db.execute_query(query)
        return result
