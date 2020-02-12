import re
import json
import requests
import random
from bs4 import BeautifulSoup
from login import get_login_session

from course import Course
from term_score_summay import TermScoreSummary
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
            result["chapterId"]
            result["examId_id"]
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

    """
    sortCriterial: "total_score_plus_bonus desc"
    DEFAULT_PAGE_SIZE: 10
    DEFAULT_PAGE_INDEX: 1
    DEFAULT_TOTLE_PAGE_COUNT: 1
    DEFAULT_TOTLE_COUNT: 0
    DEFAULT_OFFSET: 0
    pageSize: 20
    pageIndex: 1
    totlePageCount: 61
    totleCount: 1203
    offset: 0
    limit: 20
    """
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
    response = json.loads(response.content)
    summary_list = []

    for summary in response["result"]["list"]:
        term_score_summary = TermScoreSummary()
        term_score_summary.summary_id = summary["summaryId"]
        term_score_summary.term_id = summary["termId"]
        term_score_summary.member_id = summary["memberId"]
        term_score_summary.test_score = summary["testScore"]
        term_score_summary.assginment_score = summary["assignmentScore"]
        term_score_summary.exam_score = summary["examScore"]
        term_score_summary.discuss_score = summary["discussScore"]
        term_score_summary.reply_count = summary["replyCount"]
        term_score_summary.vote_count = summary["voteCount"]
        term_score_summary.outside_score = summary["outsideScore"]
        term_score_summary.total_score = summary["totalScore"]
        term_score_summary.bonus_score = summary["bonusScore"]
        term_score_summary.total_score_with_bonus = summary["totalScoreWithBonus"]
        term_score_summary.nick_name = summary["nickName"]
        term_score_summary.real_name = summary["realName"]
        term_score_summary.level = summary["level"]
        term_score_summary.final_score = summary["finalScore"]

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
