from icourse163.utils.util import camel_to_snake


class Comment(object):
    """
    id: 1437483724
    forumId: 1437467653
    postId: 1346767537
    replyId: 1436737654
    floorNumber: 6
    pageIndex: 1
    content: "<p>这道题应该选择D。</p><p><br ></p>"
    plainContent: "这道题应该选择D。"
    postTime: 1247847842371
    parentContent: "这道题应该选择D"
    plainParentContent: "这道题应该选择D"
    parentContentDeleted: 0
    posterName: "22467186恩"
    posterId: 1436743670
    postSource: "高级"
    courseId: 92741
    courseProductType: 1
    courseMode: 0
    courseChannel: 1
    termId: 4367582205
    startTime: 1437847830000
    endTime: 1327478941000
    closeVisableStatus: 0
    termPrice: 0
    schoolSN: "ZJU"
    isAnonymous: 0
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
