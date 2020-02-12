from util import camel_to_snake


class Test(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

    @property
    def allow_upload(self):
        print("Getting values")
        return self.__allow_upload

    @allow_upload.setter
    def allow_upload(self, allow_upload):
        print("Setting values")
        self.__allow_upload = allow_upload

    @property
    def analyse_setting(self):
        return self.__analyse_setting

    @analyse_setting.setter
    def analyse_setting(self, analyse_setting):
        self.__analyse_setting = analyse_setting

    @property
    def avg_score(self):
        return self.__avg_score

    @avg_score.setter
    def avg_score(self, avg_score):
        self.__avg_score = avg_score

    @property
    def chapter_id(self):
        return self.__chapter_id

    @chapter_id.setter
    def chapter_id(self, chapter_id):
        self.__chapter_id = chapter_id

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def draft_status(self):
        return self.__draft_status

    @draft_status.setter
    def draft_status(self, draft_status):
        self.__draft_status = draft_status

    @property
    def evaluate_end(self):
        return self.__evaluate_end

    @evaluate_end.setter
    def evaluate_end(self, evaluate_end):
        self.__evaluate_end = evaluate_end

    @property
    def evaluate_judge_type(self):
        return self.__evaluate_judge_type

    @evaluate_judge_type.setter
    def evaluate_judge_type(self, evaluate_judge_type):
        self.__evaluate_judge_type = evaluate_judge_type

    @property
    def evaluate_need_train(self):
        return self.__evaluate_need_train

    @evaluate_need_train.setter
    def evaluate_need_train(self, evaluate_need_train):
        self.__evaluate_need_train = evaluate_need_train

    @property
    def evaluate_score_release_time(self):
        return self.__evaluate_score_release_time

    @evaluate_score_release_time.setter
    def evaluate_score_release_time(self, evaluate_score_release_time):
        self.__evaluate_score_release_time = evaluate_score_release_time

    @property
    def evaluate_start(self):
        return self.__evaluate_start

    @evaluate_start.setter
    def evaluate_start(self, evaluate_start):
        self.__evaluate_start = evaluate_start

    @property
    def exam_id(self):
        return self.__exam_id

    @exam_id.setter
    def exam_id(self, exam_id):
        self.__exam_id = exam_id

    @property
    def gmt_create(self):
        return self.__gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        self.__gmt_create = gmt_create

    @property
    def gmt_modified(self):
        return self.__gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, gmt_modified):
        self.__gmt_modified = gmt_modified

    @property
    def test_id(self):
        return self.__test_id

    @test_id.setter
    def test_id(self, test_id):
        self.__test_id = test_id

    @property
    def is_random(self):
        return self.__is_random

    @is_random.setter
    def is_random(self, is_random):
        self.__is_random = is_random

    @property
    def mutual_evaluated(self):
        return self.__mutual_evaluated

    @mutual_evaluated.setter
    def mutual_evaluated(self, mutual_evaluated):
        self.__mutual_evaluated = mutual_evaluated

    @property
    def test_name(self):
        return self.__test_name

    @test_name.setter
    def test_name(self, test_name):
        self.__test_name = test_name

    @property
    def obj_total_score(self):
        return self.__obj_total_score

    @obj_total_score.setter
    def obj_total_score(self, obj_total_score):
        self.__obj_total_score = obj_total_score

    @property
    def objective_q_list(self):
        return self.__objective_q_list

    @objective_q_list.setter
    def objective_q_list(self, objective_q_list):
        self.__objective_q_list = objective_q_list

    @property
    def objective_score_type(self):
        return self.__objective_score_type

    @objective_score_type.setter
    def objective_score_type(self, objective_score_type):
        self.__objective_score_type = objective_score_type

    @property
    def oj_question_trytime(self):
        return self.__oj_question_trytime

    @oj_question_trytime.setter
    def oj_question_trytime(self, oj_question_trytime):
        self.__oj_question_trytime = oj_question_trytime

    @property
    def position_in_exam(self):
        return self.__position_in_exam

    @position_in_exam.setter
    def position_in_exam(self, position_in_exam):
        self.__position_in_exam = position_in_exam

    @property
    def random_setting(self):
        return self.__random_setting

    @random_setting.setter
    def random_setting(self, random_setting):
        self.__random_setting = random_setting

    @property
    def release_time(self):
        return self.__release_time

    @release_time.setter
    def release_time(self, release_time):
        self.__release_time = release_time

    @property
    def sbj_total_score(self):
        return self.__sbj_total_score

    @sbj_total_score.setter
    def sbj_total_score(self, sbj_total_score):
        self.__sbj_total_score = sbj_total_score

    @property
    def score_pub_status(self):
        return self.__score_pub_status

    @score_pub_status.setter
    def score_pub_status(self, score_pub_status):
        self.__score_pub_status = score_pub_status

    @property
    def show_analysis(self):
        return self.__show_analysis

    @show_analysis.setter
    def show_analysis(self, show_analysis):
        self.__show_analysis = show_analysis

    @property
    def submit_test_count(self):
        return self.__submit_test_count

    @submit_test_count.setter
    def submit_test_count(self, submit_test_count):
        self.__submit_test_count = submit_test_count

    @property
    def task_status(self):
        return self.__task_status

    @task_status.setter
    def task_status(self, task_status):
        self.__task_status = task_status

    @property
    def term_id(self):
        return self.__term_id

    @term_id.setter
    def term_id(self, term_id):
        self.__term_id = term_id

    # 猜测是完成时间
    @property
    def test_time(self):
        return self.__test_time

    @test_time.setter
    def test_time(self, test_time):
        self.__test_time = test_time

    @property
    def total_score(self):
        return self.__total_score

    @total_score.setter
    def total_score(self, total_score):
        self.__total_score = total_score

    @property
    def try_time(self):
        return self.__try_time

    @try_time.setter
    def try_time(self, try_time):
        self.__try_time = try_time

    # # 题目类型，2 为主观题 7为客观题
    @property
    def test_type(self):
        return self.__test_type

    @test_type.setter
    def test_type(self, test_type):
        self.__test_type = test_type

    @property
    def user_effect_status(self):
        return self.__user_effect_status

    @user_effect_status.setter
    def user_effect_status(self, user_effect_status):
        self.__user_effect_status = user_effect_status

    @property
    def user_score(self):
        return self.__user_score

    @user_score.setter
    def user_score(self, user_score):
        self.__user_score = user_score

    @property
    def user_submit_status(self):
        return self.__user_submit_status

    @user_submit_status.setter
    def user_submit_status(self, user_submit_status):
        self.__user_submit_status = user_submit_status
