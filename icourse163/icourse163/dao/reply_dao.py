from icourse163.utils.db_connection import DBConnection
from icourse163.utils.util import unicode_normalize


class ReplyDao(object):
    def __int__(self):
        pass

    def save(self, reply):
        db = DBConnection()

        param = []
        param.append(reply.id)
        param.append(reply.forum_id)
        param.append(reply.post_id)
        param.append(reply.reply_id)
        param.append(reply.floor_number)
        param.append(reply.page_index)
        param.append(unicode_normalize(reply.content))
        param.append(unicode_normalize(reply.plain_content))
        param.append(reply.post_time)
        param.append(unicode_normalize(reply.parent_content))
        param.append(unicode_normalize(reply.plain_parent_content))
        param.append(reply.parent_content_deleted)
        param.append(reply.poster_name)
        param.append(reply.poster_id)
        param.append(reply.post_source)
        param.append(reply.course_id)
        param.append(reply.course_product_type)
        param.append(reply.course_mode)
        param.append(reply.course_channel)
        param.append(reply.term_id)
        param.append(reply.start_time)
        param.append(reply.end_time)
        param.append(reply.close_visable_status)
        param.append(reply.term_price)
        param.append(reply.school_sn)
        param.append(reply.is_anonymous)

#        query = "INSERT INTO reply (id, forumId, postId, replyId, floorNumber, pageIndex, content, plainContent, postTime, parentContent, plainParentContent, parentContentDeleted, posterName, posterId, postSource, courseId, courseProductType, courseMode, courseChannel, termId, startTime, endTime, closeVisableStatus, termPrice, schoolSN, isAnonymous) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}');".format(*param)
        query = "INSERT INTO reply (id, forumId, postId, replyId, floorNumber, pageIndex, content, plainContent, postTime, parentContent, plainParentContent, parentContentDeleted, posterName, posterId, postSource, courseId, courseProductType, courseMode, courseChannel, termId, startTime, endTime, closeVisableStatus, termPrice, schoolSN, isAnonymous) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        result = db.execute_query(query, param)
        db.commit()

        return result

    def search_by_id(self, reply_id):
        db = DBConnection()
        query = "SELECT * from reply where id = {}".format(reply_id)
        result = db.execute_query(query)
        return result

    def search_all(self):
        db = DBConnection()
        query = "SELECT * from reply"
        result = db.execute_query(query)
        return result
