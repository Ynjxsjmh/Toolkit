import re
import json
import requests
import random
from bs4 import BeautifulSoup

from icourse163.utils.login import get_login_session
from icourse163.utils.util import most_common

from icourse163.domain.term import Term
from icourse163.domain.test import Test
from icourse163.domain.answer import Answer
from icourse163.domain.course import Course
from icourse163.domain.member import Member
from icourse163.domain.question import Question
from icourse163.domain.term_score_summary import TermScoreSummary

from icourse163.dao.term_dao import TermDao
from icourse163.dao.test_dao import TestDao
from icourse163.dao.answer_dao import AnswerDao
from icourse163.dao.course_dao import CourseDao
from icourse163.dao.member_dao import MemberDao
from icourse163.dao.question_dao import QuestionDao
from icourse.dao.summary_dao import SummaryDao


session = get_login_session()
http_session_id = session.cookies["NTESSTUDYSI"]


def save_terms():
    # https://www.icourse163.org/collegeAdmin/teacherPanel.htm#/agt?type=1
    request_terms_url = "https://www.icourse163.org/dwr/call/plaincall/PublishCourseBean.getTermsByTeacher.dwr"
    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'PublishCourseBean',
        'c0-methodName': 'getTermsByTeacher',
        'c0-id': 0,
        'c0-param0': 1,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    response = session.post(url=request_terms_url, data=payload).text

    object_clear_regex = re.compile(r"s\d+\.")

    term = None
    course = None
    termDao = TermDao()
    courseDao = CourseDao()

    for line in response.splitlines():
        line = object_clear_regex.sub("", line)

        try:
            result = dict(map(lambda x: x.split('=', 1), line[:-1].split(';')))
        except ValueError:
            continue

        try:
            result["courseId"]
            result["fromTermId"]
            result["id"]
            result["schoolId"]
            term = Term(result)
            termDao.save(term)
        except KeyError:
            pass

        try:
            result["id"]
            result["schoolId"]
            result["videoId"]
            result["currentTermId"]
            course = Course(result)
            courseDao.save(course)
        except KeyError:
            pass


def save_term_statistic(term_id):

    request_term_status_url = "https://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getMocTermDataStatisticDto.dwr"
    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getMocTermDataStatisticDto',
        'c0-id': 0,
        'c0-param0': term_id,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    response = session.post(url=request_term_status_url, data=payload).text

    catch_pair_regex = re.compile(r's\d+\.([^=]+)=((?:"\[[^\]]+\]"|"<p.*</p>"|[^;]+));')

    test = None
    question = None
    testDao = TestDao()
    questionDao = QuestionDao()

    for line in response.splitlines():
        result = dict(re.findall(catch_pair_regex, line))

        try:
            result["chapter_id"]
            result["exam_id"]
            result["id"]
            result["term_id"]
            test = Test(result)
            testDao.save(test)
        except KeyError:
            pass

        try:
            result["id"]
            result["test_id"]
            result["optionsDetail"]
            question = Question(result)
            questionDao.save(question)
        except KeyError:
            pass


def save_all_students_score(term_id):
    request_student_score_url = "http://www.icourse163.org/mm-tiku/web/j/mocTermScoreSummaryRpcBean.getStudentScorePagination.rpc?csrfKey={}".format(http_session_id)

    form_data = {
        "termId": term_id,
        "pIndex": 1,
        "pSize": 20,
        "rangeType": 1,
        "groupId": -1,
        "sort": 12,
        "searchName": "",
    }

    response = session.post(url=request_student_score_url, data=form_data).text
    response = json.loads(response)
    form_data["pSize"] = response["result"]["query"]["totleCount"]
    response = session.post(url=request_student_score_url, data=form_data).text
    response = json.loads(response)

    summary = None
    summaryDao = SummaryDao()

    for summary in response["result"]["list"]:
        term_score_summary = TermScoreSummary(summary)

        summaryDao.save(term_score_summary)


def save_student_score_detail(member_id, term_id):
    request_student_score_detail_url = "http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getSingleStudentScores.dwr"

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getSingleStudentScores',
        'c0-id': 0,
        'c0-param0': member_id,
        'c0-param1': term_id,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    response = session.post(url=request_student_score_detail_url, data=payload).text

    catch_pair_regex = re.compile(r's\d+\.([^=]+)=([^;]+);')
    answer = None
    answerDao = AnswerDao()

    for line in response.splitlines():
        result = dict(re.findall(catch_pair_regex, line))

        try:
            if result["id"] == 'null':
                continue
            result["aid"]
            result["answerer_id"]
            result["exam_id"]
            result["test_id"]
            result["tid"]
            answer = Answer(result)
            answerDao.save(answer)
        except KeyError:
            pass


def save_student(term_id):
    # http://www.icourse163.org/collegeAdmin/termManage/1206772205.htm#/tp/cdata?t=1&tid=1220061747
    request_student_in_term_url = "http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getStudentTestAggreScores.dwr"

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getStudentTestAggreScores',
        'c0-id': 0,
        'c0-param0': term_id,
        'c0-param1': 20,
        'c0-param2': 1,
        'c0-param3': "",
        'c0-param4': 1,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    response = session.post(url=request_student_in_term_url, data=payload).text

    info_regex = re.compile(r".*limit=(?P<limit>\d+).*offset=(?P<offset>\d+).*totleCount=(?P<totleCount>\d+)")
    info_match = re.search(info_regex, response)

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'MocScoreManagerBean',
        'c0-methodName': 'getStudentTestAggreScores',
        'c0-id': 0,
        'c0-param0': term_id,
        'c0-param1': info_match.group("totleCount"),
        'c0-param2': 1,
        'c0-param3': "",
        'c0-param4': 1,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    response = session.post(url=request_student_in_term_url, data=payload).text

    obj_regex = re.compile(r'(s\d+\.)')
    member = None
    memberDao = MemberDao()

    for line in response.splitlines():
        result = re.findall(obj_regex, line)
        obj = most_common(result)
        results = line.split(obj)
        result_list = []

        for result in results:
            if result == "":
                pass
            else:
                result_list.append(result[:-1].split("=", 1))

        result = dict(result_list)

        try:
            result["id"]
            result["email"]
            result["nickname"]
            result["realname"]
            member = Member(result)
            memberDao.save(member)
        except KeyError:
            pass


if __name__ == "__main__":
    session = get_login_session()
    http_session_id = session.cookies["NTESSTUDYSI"]

    # 答题记录 - 单元测验
    # http://www.icourse163.org/learn/JLU-62001?tid=1206772205&_trace_c_p_k2_=78e55f8bff9d4be3bda1161d877f18bc#/learn/quizscore?id=1220061754&aid=1481357597

    request_quiz_result_url = "http://www.icourse163.org/dwr/call/plaincall/MocQuizBean.getQuizPaperDto.dwr"

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'MocQuizBean',
        'c0-methodName': 'getQuizPaperDto',
        'c0-id': 0,
        'c0-param0': id,
        'c0-param1': aid,
        'c0-param2': 'true',
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    # 答题记录 - 单元作业
    # http://www.icourse163.org/learn/JLU-62001?tid=1206772205&_trace_c_p_k2_=40493107bde44512910441163f9bdac6#/learn/ojhw?id=1220061748&aid=1466334466&isCheck=1
    request_quiz_submit_records = "http://www.icourse163.org/dwr/call/plaincall/YocOJQuizBean.adminGetOjQuestionSubmitRecords.dwr"

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'YocOJQuizBean',
        'c0-methodName': 'adminGetOjQuestionSubmitRecords',
        'c0-id': 0,
        'c0-param0': id,
        'c0-param1': 'false',
        'c0-param2': aid,
        'batchId': random.randint(1000000000000, 20000000000000)
    }

    # 答题记录 - 课程考试（客观题）
    # http://www.icourse163.org/learn/JLU-62001?tid=1206772205&_trace_c_p_k2_=d66580f2348144909fb0175846cc712c#/learn/examObjectScore?id=1220061796&aid=1553103973&isCheck=1
    # 同 答题记录 - 单元测验

    # 答题记录 - 课程考试（主观题）
    # http://www.icourse163.org/learn/JLU-62001?tid=1206772205&_trace_c_p_k2_=b28950ebdc3f4d02b0d3bb90b5c2cf9e#/learn/examOj?id=1220061797&aid=1544038649&isCheck=1
    # 同 答题记录 - 单元作业

    ask_video_url = "http://www.icourse163.org/dwr/call/plaincall/MocScoreManagerBean.getStudentScoresByExamId.dwr"

#    resp = session.post(url=ask_video_url, data=payload).text

    payload = {
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': http_session_id,
        'c0-scriptName': 'CourseBean',
        'c0-methodName': 'getLastLearnedMocTermDto',
        'c0-id': 0,
        'c0-param0': 1206772205,
        'batchId': random.randint(1000000000000, 20000000000000)
     }
    cs_url = 'http://www.icourse163.org/dwr/call/plaincall/CourseBean.getLastLearnedMocTermDto.dwr'
#    rdata = session.post(cs_url, data=payload, timeout=None).text
