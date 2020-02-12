from util import camel_to_snake


class Term(object):
    """
    'achievement_status': '0'
    'apply_convert_channel_status': 'null'
    'apply_mooc_status': '0'
    'apply_passed_term_id': 'null'
    'asyn_price': 'null'
    'big_photo_url': 'http://edu-image.nosdn.127.net/EFD03FFF024EEB94531EF37CFCEC62F3.jpg'
    'cert_apply_end_time': 'null'
    'cert_apply_start_time': 'null'
    'cert_no': 'null'
    'cert_status': '10'
    'charge_cert_status': '10'
    'chargeable_cert': '1'
    'close_visable_status': '1'
    'copied': '1'
    'copy_right': 'null'
    'copy_time': 'null'
    'course_id': '72641'
    'course_name': 'null'
    'duration': '""'
    'end_time': '1590422400000'
    'enroll_count': '281'
    'from_term_id': '1932142345'
    'from_term_mode': '0'
    'has_enroll': 'true'
    'id': '1238916433'
    'json_content': '本课程面向无编程基础'
    'lector_panels': 's0'
    'lessons_count': '0'
    'mode': '0'
    'order_price': 'null'
    'ordinary_editors': 'null'
    'origin_moc_term_copy_right': 'null'
    'original_course_channel': 'null'
    'original_price': '0.00'
    'price': '0.00'
    'publish_status': '2'
    'school_id': '2934'
    'school_panel': 'null'
    'score_card_dto': 'null'
    'self_moc_term_copyright': 'null'
    'special_chargeable_term': 'false'
    'spoc_to_ooc_status': '0'
    'start_time': '1582336800000'
    'sync_price': 'null'
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    @property
    def from_term_id(self):
        return self.__from_term_id

    @from_term_id.setter
    def from_term_id(self, from_term_id):
        self.__from_term_id = from_term_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id

    @property
    def school_id(self):
        return self.__school_id

    @school_id.setter
    def school_id(self, school_id):
        self.__school_id = school_id

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time

    @property
    def achievement_status(self):
        return self.__achievement_status

    @achievement_status.setter
    def achievement_status(self, achievement_status):
        self.__achievement_status = achievement_status

    @property
    def enroll_count(self):
        return self.__enroll_count

    @enroll_count.setter
    def enroll_count(self, enroll_count):
        self.__enroll_count = enroll_count

    @property
    def json_content(self):
        return self.__json_content

    @json_content.setter
    def json_content(self, json_content):
        self.__json_content = json_content

    @property
    def lessons_count(self):
        return self.__lessons_count

    @lessons_count.setter
    def lessons_count(self, lessons_count):
        self.__lessons_count = lessons_count

    @property
    def publish_status(self):
        return self.__publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        self.__publish_status = publish_status
