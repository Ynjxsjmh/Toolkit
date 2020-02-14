from icourse163.utils.util import camel_to_snake


class Member(object):
    """
    'accountType': 'null'
    'birthDay': 'null'
    'description': 'null'
    'email': 'null'
    'emailActive': '2'
    'enable': 'null'
    'epayAccount': 'null'
    'epayAccountState': 'null'
    'fromAppInfoId': 'null'
    'fromAppInfoType': 'null'
    'gmtCreate': 'new Date(3232438989787)'
    'gmtModified': 'new Date(2894398490407)'
    'id': '1399441731'
    'idNumber': 'null'
    'idType': 'null'
    'largeFaceUrl': '"http0";
    'lastLogonTime=new Date(1568635744787)
    'lastLongIP=null
    'loginId=null
    'loginType=null
    'memberFrom=50
    'moocLastLogonTime=null
    'nickName="532"
    'personalUrlSuffix="mooc71238932989805699"
    'phoneNumber=null
    'qqNumber=null
    'realName="单单"
    'sex=1
    'signature=null
    'skills=null
    smallFaceUrl="http://edu-image.nosdn.127.n0y180&amp;quality=100"'
    'studentNumber': 'null'
    'userName': 'null'
    """
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])

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
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, group_id):
        self.__group_id = group_id
