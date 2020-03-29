from icourse163.utils.util import camel_to_snake


class AnswerDetail(object):
    """
    MocQuizBean.getQuizPaperDto.dwr
    tid=2389743987
    aid=3284932485
    选择题
    answerTimes=null
    content=null
    correct=0
    correctCount=0
    evalResult=null
    evaluateDto=null
    lastAnswerId=null
    maxScoreAnswerId=null
    modifyPlatForm=0
    ojLanguage=0
    ojResultDto=null
    ojStatus=null
    optIds=s8
    qCorrectCount=1
    qid=3289434243
    score=2.00
    time=null
    type=1

    YocOJQuizBean.getOJPaperDto.dwr
    tid=8324984747
    aid=3289452525
    OJ 题
    answerTimes=3
    content=s9
    correct=null
    correctCount=null
    evalResult=null
    evaluateDto=null
    lastAnswerId=3824780855
    maxScoreAnswerId=3243450855
    modifyPlatForm=0
    ojLanguage=0
    ojResultDto=s10
    ojStatus=30
    optIds=null
    qCorrectCount=null
    qid=3289984253
    score=10
    time=null
    type=7
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
