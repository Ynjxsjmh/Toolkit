from icourse163.utils.util import camel_to_snake


class Answer(object):
    """
    'aggreId': 'null'
    'aggreScore': 's1'
    'aid': '1829312833'
    'answererId': '2983292189'   // member_id 别名
    'deadline': '8329843902930'
    'draftSubjConfirmed': 'null'
    'draftSubjectiveBonusScore': 'null'
    'effectStatus': '10'
    'email': 'null'
    'evaluates': 'null'
    'examId': '-1'
    'finalScore': '12.66'
    'id': '1829312833'
    'mocAuthenticatedMemberDto': 'null'
    'name': '第八讲'
    'nickname': '23299821'
    'objectiveScore': '12.66'
    'reviewStatus': 'null'
    'score': '12.66'
    'scorePubStatus': '0'
    'showScore': 'true'
    'studentNumber': 'null'
    'subMocAnswerForms': 'null'
    'subjectiveScore': 'null'
    'submitTime': '2389843903075'
    'testId': '8397328780'
    'tid': '8397328780'
    'totalScore': '14.0'
    'type': '2'
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

    @property
    def answer_id(self):
        return self.__answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        self.__answer_id = answer_id

    # alias for member_id
    @property
    def answerer_id(self):
        return self.__answerer_id

    @answerer_id.setter
    def answerer_id(self, answerer_id):
        self.__answerer_id = answerer_id
