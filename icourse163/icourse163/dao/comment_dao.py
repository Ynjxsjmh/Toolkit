from icourse163.utils.db_connection import DBConnection
from icourse163.utils.util import unicode_normalize


class CommentDao(object):
    def __int__(self):
        pass

    def save(self, comment):
        db = DBConnection()

        param = []
        param.append(comment.id)
        param.append(comment.forum_id)
        param.append(comment.post_id)
        param.append(comment.reply_id)
        param.append(comment.floor_number)
        param.append(comment.page_index)
        param.append(unicode_normalize(comment.content))
        param.append(unicode_normalize(comment.plain_content))
        param.append(comment.post_time)
        param.append(unicode_normalize(comment.parent_content))
        param.append(unicode_normalize(comment.plain_parent_content))
        param.append(comment.parent_content_deleted)
        param.append(comment.poster_name)
        param.append(comment.poster_id)
        param.append(comment.post_source)
        param.append(comment.course_id)
        param.append(comment.course_product_type)
        param.append(comment.course_mode)
        param.append(comment.course_channel)
        param.append(comment.term_id)
        param.append(comment.start_time)
        param.append(comment.end_time)
        param.append(comment.close_visable_status)
        param.append(comment.term_price)
        param.append(comment.school_sn)
        param.append(comment.is_anonymous)

        query = "INSERT INTO comment (id, forumId, postId, replyId, floorNumber, pageIndex, content, plainContent, postTime, parentContent, plainParentContent, parentContentDeleted, posterName, posterId, postSource, courseId, courseProductType, courseMode, courseChannel, termId, startTime, endTime, closeVisableStatus, termPrice, schoolSN, isAnonymous) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        result = db.execute_query(query, param)
        db.commit()

        return result

    def search_by_id(self, comment_id):
        db = DBConnection()
        query = "SELECT * from comment where id = {}".format(comment_id)
        result = db.execute_query(query)
        return result

    def search_all(self):
        db = DBConnection()
        query = "SELECT * from comment"
        result = db.execute_query(query)
        return result
