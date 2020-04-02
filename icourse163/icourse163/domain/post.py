from icourse163.utils.util import camel_to_snake


class Post(object):
    """
    id: 3284783996
    type: 2
    postTime: 1324893030212
    title: "函数的？"
    anonymous: 0
    tagAgree: 0
    tagTop: 0
    tagTopTime: 0
    tagSolve: 0
    tagLector: 0
    countBrowse: 30
    countReply: 7
    countVote: 0
    lastReplyTime: 8495540104162
    lastReplyerId:
    posterId:
    relateUnit: null
    unreadCount: null
    content: null
    lectorOrAssistFlag: null
    hasVoteUp: false
    deleted: 0
    shortIntroduction: "如题？"
    pictures: ""
    postSource: "高级"
    courseId: 43671
    courseProductType: 1
    courseMode: 0
    courseChannel: 1
    termId: 1434783755
    startTime: 2439309548000
    endTime: 3443789000000
    closeVisableStatus: 0
    termPrice: 0
    forumId: 1894473484
    schoolSN: "ZJU"
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
