from icourse163.util import camel_to_snake


class Question(object):
    """
    'allowUpload': 'null'
    'analyse': 'null'
    'description': '<p></p>'
    'fillblankType': 'null'
    'gmtCreate': '1551272585032'
    'gmtModified': '1577668049717'
    'id': '1217514521'
    'judgeDtos': 'null'
    'judgerules': 'null'
    'ojCases': 's220'
    'ojMemLimit': '131072000'
    'ojNeedInput': 'true'
    'ojSupportedLanguage': '1'
    'ojSupportedLanguageList': 's221'
    'ojTimeLimit': '2000'
    'ojTryTime': '5'
    'optionDtos': 'null'
    'options': 'null'
    'optionsDetail': 'null'
    'plainTextTitle': '组合数计算'
    'position': '1'
    'sampleAnswerJson': 'null'
    'sampleAnswers': 'null'
    'score': '15.00'
    'stdAnswer': 'null'
    'testId': '8239439897'
    'title': '组合数'
    'titleAttachment': 'null'
    'titleAttachmentDtos': 'null'
    'type': '7'
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
