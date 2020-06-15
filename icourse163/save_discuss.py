import time

from icourse163.dao.post_dao import PostDao
from icourse163.dao.reply_dao import ReplyDao
from icourse163.dao.comment_dao import CommentDao
from icourse163.dao.summary_dao import SummaryDao
from icourse163.icourse163 import *

from icourse163.utils.util import raw_unicode_escape


post_dao = PostDao()
reply_dao = ReplyDao()
comment_dao = CommentDao()
summary_dao = SummaryDao()


def get_member_from_summary(term_id):
    query = """
            SELECT memberId
            FROM summary
            WHERE termId={}
            """.format(term_id)
    print(query)
    return summary_dao.select_query(query)


def get_index(last_stored_id, lists):
    """
    获取上一个保存的id在lists中的索引
    没找到就返回 -1
    """
    for index, current in enumerate(lists):
        if current[0] == last_stored_id:
            break
        else:
            index = -1
    return index


def save(member_list):
    i = 0
    for member in member_list:
        print(f"Saving user {member[0]} ...")
        save_user_post(member[0])
        save_user_reply(member[0])
        save_user_comment(member[0])
        i += 1
        if i % 2 == 0:
            time.sleep(4)


terms_id = [1003251017, 1206772205]
start_time = time.time()
member_list = []

for term_id in terms_id:
    print(term_id)
    member_list.extend(get_member_from_summary(term_id))

# last_stored_member_id = member_list[0][0]
last_stored_member_id = '1403742452'
index = get_index(last_stored_member_id, member_list)

print("----------")
print(index)
member_list = member_list[index:]

save(member_list)

end_time = time.time()
print("takes...")
print(end_time - start_time)
