from icourse163.utils.util import camel_to_snake


class Exam(object):
    """
    avgScore=106.21
    bonusScore=null
    contentType=4
    deadline=1577633400000
    description="\u672C\u3002"
    draftStatus=0
    gmtCreate=1568522861583
    gmtModified=1577668049973
    id=1832984921
    judgeType=3
    name="\u300A\u9AD8\u8BA1\u300B\u671F\u672B\u8003\u8BD5"
    objectTest=s4
    objectTestId=8283200796
    objectTestVo=null
    releaseTime=1576425600000
    scorePubStatus=2
    scoreReleaseTime=1329847378900
    subjectTest=s5
    subjectTestId=1220061797
    subjectTestVo=null
    submitTestCount=1039
    taskStatus="published"
    termId=1206772205
    totalScore=120.00
    userScore=null
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
