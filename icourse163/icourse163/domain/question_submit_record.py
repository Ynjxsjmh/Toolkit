from icourse163.utils.util import camel_to_snake


class QuestionSubmitRecord(object):
    """
    YocOJQuizBean.adminGetOjQuestionSubmitRecords.dwr
    testId=1283439748
    answerId=1328934466

    isMaxScore=true
    language=0
    ojSubmitTime=1569328579776
    questionId=2390438952
    score=10
    status=30
    testAnswerformId=1328934466   ;; answerId 的别称
    testId=1283439748
    userId=1489348329
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
