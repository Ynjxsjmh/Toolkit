from icourse163.utils.util import camel_to_snake


class Course(object):
    """
    'all_terms': 's6'        // 没用
    'apply_convert_channel_status': '0'
    'apply_mooc_status': '0'
    'channel': '1'
    'classroom_support': 'null'
    'course_type': '1'
    'current_term_chargeable': '0'
    'current_term_id': '1450396448'   // 当前学期 id
    'first_publish_time': '0'
    'from_course_id': '-1'
    'from_course_mode': '-1'
    'from_course_name': 'null'
    'from_course_school_name': 'null'
    'gmt_create': '1406081987056'
    'id': '62001'                    // 课程 id
    'img_url': '"http://edu-image.nosdn.127.net/EFD03FFF024C62F3.jpg?imageView&thumbnail=510y288&quality=100"'
    'last_learning_time': 'null'
    'learned_count': 'null'
    'learner_count': '52131'
    'moc_tag_dtos': 's7'
    'mode': '0'
    'name': '"来啦怪丹佛个大类"'    // 课程名称
    'ordinary_editors': 's8'
    'original_course_channel': '0'
    'product_type': '1'
    'school_id': '3049'             // 学校 id
    'school_img_url': '"http://img2.ph.126.net/fehABjVTEaEhheiJK-Fw==/.jpg"'
    'school_panel':'s9'
    'short_name': '"932joael23"'    // 代号
    'spoc_to_ooc_status': '0'
    'status': '2'
    'term_panel': 's10'
    'universal_coupon': 'null'
    'video_id': '1239023871'
    'video_url': '"nos/mp4/2017/06/14/32_dskdjs990f23029384faa9a7db53cc32_sd.mp4"'
    'web_visible': '1'
    'weight': '0'}
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        self.course_id = id

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        self.course_name = name

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    @property
    def short_name(self):
        return self.__short_name

    @short_name.setter
    def short_name(self, short_name):
        self.__short_name = short_name
        self.__course_short_name = short_name

    @property
    def course_short_name(self):
        return self.__course_short_name

    @course_short_name.setter
    def course_short_name(self, course_short_name):
        self.__course_short_name = course_short_name
