from util import camel_to_snake


class TermScoreSummary(object):
    """
    'summary_id': 1223122009
    'term_id': 1202772305
    'member_id': 1401292023
    'test_score': 146.0
    'assignment_score': 480.0
    'exam_score': 120.0
    'discuss_score': 100.0
    'reply_count': 31
    'vote_count': 1
    'outside_score': None
    'total_score': 100.0
    'bonus_score': None
    'total_score_with_bonus': 100.0
    'cert_type_now': 0
    'nick_name': '123晓明'
    'real_name': '晓明'
    'student_number': None
    'group_id': None
    'group_name': None
    'school_name': None
    'departments': None
    'professional': None
    'clazz': None
    'comment': None
    'level': '优秀'
    'final_score': 100.0
    """
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

    @property
    def summary_id(self):
        return self.__summary_id

    @summary_id.setter
    def summary_id(self, summary_id):
        self.__summary_id = summary_id

    @property
    def term_id(self):
        return self.__term_id

    @term_id.setter
    def term_id(self, term_id):
        self.__term_id = term_id

    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id

    @property
    def test_score(self):
        return self.__test_score

    @test_score.setter
    def test_score(self, test_score):
        self.__test_score = test_score

    @property
    def assignment_score(self):
        return self.__assignment_score

    @assignment_score.setter
    def assignment_score(self, assignment_score):
        self.__assignment_score = assignment_score

    @property
    def exam_score(self):
        return self.__exam_score

    @exam_score.setter
    def exam_score(self, exam_score):
        self.__exam_score = exam_score

    @property
    def discuss_score(self):
        return self.__discuss_score

    @discuss_score.setter
    def discuss_score(self, discuss_score):
        self.__discuss_score = discuss_score

    @property
    def reply_count(self):
        return self.__reply_count

    @reply_count.setter
    def reply_count(self, reply_count):
        self.__reply_count = reply_count

    @property
    def vote_count(self):
        return self.__vote_count

    @vote_count.setter
    def vote_count(self, vote_count):
        self.__vote_count = vote_count

    @property
    def outside_score(self):
        return self.__outside_score

    @outside_score.setter
    def outside_score(self, outside_score):
        self.__outside_score = outside_score

    @property
    def total_score(self):
        return self.__total_score

    @total_score.setter
    def total_score(self, total_score):
        self.__total_score = total_score

    @property
    def bonus_score(self):
        return self.__bonus_score

    @bonus_score.setter
    def bonus_score(self, bonus_score):
        self.__bonus_score = bonus_score

    @property
    def total_score_with_bonus(self):
        return self.__total_score_with_bonus

    @total_score_with_bonus.setter
    def total_score_with_bonus(self, total_score_with_bonus):
        self.__total_score_with_bonus = total_score_with_bonus

    @property
    def nick_name(self):
        return self.__nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        self.__nick_name = nick_name

    @property
    def real_name(self):
        return self.__real_name

    @real_name.setter
    def real_name(self, real_name):
        self.__real_name = real_name

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, student_number):
        self.__student_number = student_number

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, group_id):
        self.__group_id = group_id

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, group_name):
        self.__group_name = group_name

    @property
    def school_name(self):
        return self.__school_name

    @school_name.setter
    def school_name(self, school_name):
        self.__school_name = school_name

    @property
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, departments):
        self.__departments = departments

    @property
    def professional(self):
        return self.__professional

    @professional.setter
    def professional(self, professional):
        self.__professional = professional

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def final_score(self):
        return self.__final_score

    @final_score.setter
    def final_score(self, final_score):
        self.__final_score = final_score
