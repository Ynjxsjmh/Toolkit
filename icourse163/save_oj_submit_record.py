import time

from icourse163.dao.term_dao import TermDao
from icourse163.dao.course_dao import CourseDao
from icourse163.dao.answer_dao import AnswerDao
from icourse163.dao.summary_dao import SummaryDao
from icourse163.dao.case_result_dao import CaseResultDao
from icourse163.domain.term import Term
from icourse163.icourse163 import *

from icourse163.utils.util import raw_unicode_escape

terms_id = [1003251017, 1206772205]

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
    print(query)
    return answer_dao.select_query(query)


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
            save_submit_record(test_id, answer_id)


terms_id = [1003251017, 1206772205]
start_time = time.time()
answer_list = []

for term_id in terms_id:
    print(term_id)
    answer_list.extend(get_answer_in_term(term_id))

save(answer_list)

end_time = time.time()
print("takes...")
print(end_time - start_time)
