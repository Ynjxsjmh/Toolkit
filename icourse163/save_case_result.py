import time
import sys

from icourse163.dao.term_dao import TermDao
from icourse163.dao.course_dao import CourseDao
from icourse163.dao.answer_dao import AnswerDao
from icourse163.dao.summary_dao import SummaryDao
from icourse163.dao.case_result_dao import CaseResultDao
from icourse163.domain.term import Term
from icourse163.icourse163 import *

from icourse163.utils.util import raw_unicode_escape


answer_dao = AnswerDao()
summary_dao = SummaryDao()


def get_answer_in_term(term_id):
    query = """
            SELECT *
            FROM answer
            WHERE answererId IN (SELECT memberId
                                 FROM summary
                                 WHERE termId={})
            """.format(term_id)

    return answer_dao.select_query(query)

    # summarys = summary_dao.search_by_term_id(term_id)

    # for summary in summarys:
    #     member_id = summary[2]
    #     answers = answer_dao.search_by_answerer_id(member_id)
    #     answer_list.extend(answers)

    # return answer_list


def save(answer_list):
    i = 0
    for answer in answer_list:
        answer_id = answer[0]
        test_id = answer[15]
        typee = answer[-1]
        # case result 是针对 OJ 题型的，type 为7的是OJ题
        if typee == "7" or typee == 7:
            i = i+1
            if i % 50 == 0:
                time.sleep(2)
                save_case_result(test_id, answer_id)


def get_index(last_stored_answer_id, answer_list):
    for index, answer in enumerate(answer_list):
        if answer[0] == last_stored_answer_id:
            break
        else:
            index = -1
    return index


def get_unstored_list(last_stored_answer_id, term_id):
    answer_list = get_answer_in_term(term_id)

    if last_stored_answer_id == -1:
        return answer_list
    else:
        index = get_index(last_stored_answer_id, answer_list)
        if index == -1:  # 不在有两种可能，一种是存过了，一种是没存到
            return []
        return answer_list[index:]


def write_complete_message(message):
    with open("log.txt", "a") as f:
        f.write(str(message)+'done \n')


terms_id = [1003251017, 1206772205]

last_stored_answer_id = 1149907469

start_time = time.time()

# for term_id in terms_id:
#     answer_list = get_unstored_list(last_stored_answer_id, term_id)
#     save(answer_list)
#     write_complete_message(term_id)

answer_list = []

for term_id in terms_id:
    print(term_id)
    answer_list.extend(get_answer_in_term(term_id))

index = get_index(last_stored_answer_id, answer_list)

answer_list = answer_list[index:]

save(answer_list)

end_time = time.time()
print("takes...")
print(end_time - start_time)
# 961.6100
