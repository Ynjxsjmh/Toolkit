from icourse163.utils.util import camel_to_snake


class CaseResult(object):
    """
    YocOJQuizBean.getOJPaperDto.dwr
    testId
    answerId

    caseId=1203878920
    inputDataUrl=null
    inputNosKey=null
    outpuDataUrl=null
    outputNosKey=null
    pass=true
    result="ACCEPTED"
    score=4
    tips=""
    usedCpuTime=2
    usedMemory=135168
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
