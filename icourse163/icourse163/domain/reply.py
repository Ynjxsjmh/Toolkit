from icourse163.utils.util import camel_to_snake


class Reply(object):
    """
    id: 1439483893
    forumId: 1438748384
    postId: 1437838757
    replyId: null
    floorNumber: 21
    pageIndex: 2
    content: "sizeof的"
    plainContent: "sizeof的"
    postTime: 1472784783749
    parentContent: "strlen"
    plainParentContent: "strlen"
    parentContentDeleted: 0
    posterName: "551438743 "
    posterId: 1328487013
    postSource: "高级"
    courseId: 23841
    courseProductType: 1
    courseMode: 0
    courseChannel: 1
    termId: 1467312895
    startTime: 1267499358000
    endTime: 1498398535700
    closeVisableStatus: 0
    termPrice: 0
    schoolSN: "ZJU"
    isAnonymous: null
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
