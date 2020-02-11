# s13.achievementStatus=1;s13.applyConvertChannelStatus=null;s13.applyMoocStatus=0;s13.applyPassedTermId=null;s13.asynPrice=null;s13.bigPhotoUrl="http://edu-image.nosdn.127.net/E2A2D9422AE2D9E37C24A59A94984CB8.png?imageView&thumbnail=510y288&quality=100";s13.certApplyEndTime=null;s13.certApplyStartTime=null;s13.certNo=null;s13.certStatus=20;s13.chargeCertStatus=20;s13.chargeableCert=1;s13.closeVisableStatus=0;s13.copied=1;s13.copyRight=null;s13.copyTime=null;s13.courseId=62001;s13.courseName=null;s13.duration="";s13.endTime=1561563000000;s13.enrollCount=1763;s13.fromTermId=1003251017;s13.fromTermMode=0;s13.hasEnroll=true;s13.id=1206088220;s13.lectorPanels=s34;s13.lessonsCount=72;s13.mode=0;s13.orderPrice=null;s13.ordinaryEditors=null;s13.originMocTermCopyRight=null;s13.originalCourseChannel=null;s13.originalPrice=0.00;s13.price=0.00;s13.publishStatus=2;s13.schoolId=8008;s13.schoolPanel=null;s13.scoreCardDto=null;s13.selfMocTermCopyright=null;s13.specialChargeableTerm=false;s13.spocToOocStatus=0;s13.startTime=1553479200000;s13.syncPrice=null;
# s13.jsonContent="spContent=";


class Course(object):
    def __init__(self):
        pass

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


course = Course()
course.course_id = 1000
print(course.course_id)
