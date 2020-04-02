from icourse163.utils.db_connection import DBConnection


class PostDao(object):
    def __int__(self):
        pass

    def save(self, post):
        db = DBConnection()

        param = []
        param.append(post.id)
        param.append(post.type)
        param.append(post.post_time)
        param.append(post.title)
        param.append(post.anonymous)
        param.append(post.tag_agree)
        param.append(post.tag_top)
        param.append(post.tag_top_time)
        param.append(post.tag_solve)
        param.append(post.tag_lector)
        param.append(post.count_browse)
        param.append(post.count_reply)
        param.append(post.count_vote)
        param.append(post.last_reply_time)
        param.append(post.last_replyer_id)
        param.append(post.poster_id)
        param.append(post.relate_unit)
        param.append(post.unread_count)
        param.append(post.content)
        param.append(post.lector_or_assist_flag)
        param.append(post.has_vote_up)
        param.append(post.deleted)
        param.append(post.short_introduction)
        param.append(post.pictures)
        param.append(post.post_source)
        param.append(post.course_id)
        param.append(post.course_product_type)
        param.append(post.course_mode)
        param.append(post.course_channel)
        param.append(post.term_id)
        param.append(post.start_time)
        param.append(post.end_time)
        param.append(post.close_visable_status)
        param.append(post.term_price)
        param.append(post.forum_id)
        param.append(post.school_sn)

        query = "INSERT INTO post (id, type, postTime, title, anonymous, tagAgree, tagTop, tagTopTime, tagSolve, tagLector, countBrowse, countReply, countVote, lastReplyTime, lastReplyerId, posterId, relateUnit, unreadCount, content, lectorOrAssistFlag, hasVoteUp, deleted, shortIntroduction, pictures, postSource, courseId, courseProductType, courseMode, courseChannel, termId, startTime, endTime, closeVisableStatus, termPrice, forumId, schoolSN) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}', '{31}', '{32}', '{33}', '{34}', '{35}');".format(*param)

        result = db.execute_query(query)
        db.commit()

        return result

    def search_by_id(self, post_id):
        db = DBConnection()
        query = "SELECT * from post where id = {}".format(post_id)
        result = db.execute_query(query)
        return result

    def search_all(self):
        db = DBConnection()
        query = "SELECT * from post"
        result = db.execute_query(query)
        return result
