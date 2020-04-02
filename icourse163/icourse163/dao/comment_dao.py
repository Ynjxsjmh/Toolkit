from icourse163.utils.db_connection import DBConnection


class CommentDao(object):
    def __int__(self):
        pass

    def save(self, comment):
        db = DBConnection()

        param = []
        param.append(comment.id)
        param.append(comment.forum_id)
        param.append(comment.post_id)
        param.append(comment.comment_id)
        param.append(comment.floor_number)
        param.append(comment.page_index)
        param.append(comment.content)
        param.append(comment.plain_content)
        param.append(comment.post_time)
        param.append(comment.parent_content)
        param.append(comment.plain_parent_content)
        param.append(comment.parent_content_deleted)
        param.append(comment.poster_name)
        param.append(comment.poster_id)
        param.append(comment.poster_source)
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

        query = "INSERT INTO comment (id, forumId, postId, commentId, floorNumber, pageIndex, content, plainContent, postTime, parentContent, plainParentContent, parentContentDeleted, posterName, posterId, postSource, courseId, courseProductType, courseMode, courseChannel, termId, startTime, endTime, closeVisableStatus, termPrice, schoolSN, isAnonymous) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}');".format(*param)

        result = db.execute_query(query)
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
