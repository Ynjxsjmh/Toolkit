import re
import json
import requests
import random
from bs4 import BeautifulSoup
from login import get_login_session

from course import Course
from term_score_summary import TermScoreSummary
from test import Test


def get_terms():
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

    course_list = []

    for line in response.splitlines():
        line = object_clear_regex.sub("", line)
        result = dict(map(lambda x: x.split('='), line[:-1].split(';')))

        try:
            result["course_id"]
            result["from_term_id"]
            result["id"]
            result["school_id"]
            course = Course(result)
            course_list.append(course)
        except KeyError:
            pass

    return course_list


def get_term_statistic():

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

    object_clear_regex = re.compile(r"s\d+\.")
    test_list = []

    for line in response.splitlines():
        line = object_clear_regex.sub("", line)
        result = dict(map(lambda x: x.split('='), line[:-1].split(';')))

        try:
            result["chapter_d"]
            result["exam_id"]
            result["id"]
            result["term_id"]
            test = Test(result)
            test_list.append(test)
        except KeyError:
            pass

    return test_list


def get_all_students_score():
    # http://www.icourse163.org/collegeAdmin/termManage/1206772205.htm#/tp/manageStudent
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
    summary_list = []

    for summary in response["result"]["list"]:
        term_score_summary = TermScoreSummary(summary)

        summary_list.append(term_score_summary)

    return summary_list


def get_student_score_detail():
    # http://www.icourse163.org/collegeAdmin/termManage/1206772205.htm#/tp/manageStudent?t=2&mid=1401331329
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

    # s13.achievementStatus=1;s13.applyConvertChannelStatus=null;s13.applyMoocStatus=0;s13.applyPassedTermId=null;s13.asynPrice=null;s13.bigPhotoUrl="http://edu-image.nosdn.127.net/E2A2D9422AE2D9E37C24A59A94984CB8.png?imageView&thumbnail=510y288&quality=100";s13.certApplyEndTime=null;s13.certApplyStartTime=null;s13.certNo=null;s13.certStatus=20;s13.chargeCertStatus=20;s13.chargeableCert=1;s13.closeVisableStatus=0;s13.copied=1;s13.copyRight=null;s13.copyTime=null;
    # s13.courseId=62001;s13.courseName=null;s13.duration="";s13.endTime=1561563000000;s13.enrollCount=1763;s13.fromTermId=1003251017;s13.fromTermMode=0;s13.hasEnroll=true;s13.id=1206088220;s13.lectorPanels=s34;s13.lessonsCount=72;s13.mode=0;s13.orderPrice=null;s13.ordinaryEditors=null;s13.originMocTermCopyRight=null;s13.originalCourseChannel=null;s13.originalPrice=0.00;s13.price=0.00;s13.publishStatus=2;s13.schoolId=8008;s13.schoolPanel=null;s13.scoreCardDto=null;s13.selfMocTermCopyright=null;s13.specialChargeableTerm=false;s13.spocToOocStatus=0;s13.startTime=1553479200000;s13.syncPrice=null;
    course_regex = re.compile(r".*achievementStatus=(?P<achievementStatus>\d+).*courseId=(?P<courseId>\d+).*endTime=(?P<endTime>\d+).*enrollCount=(?P<enrollCount>\d+).*fromTermId=(?P<fromTermId>\d+).*id=(?P<id>\d+).*lessonsCount=(?P<lessonsCount>\d+).*publishStatus=(?P<publishStatus>\d+).*schoolId=(?P<schoolId>\d+).*startTime=(?P<startTime>\d+)")
    course_list = []

    for line in response.splitlines():
        course_match = re.search(course_regex, line)

        course = Course()
        course.achievement_status = course_match.group("achievementStatus")


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
