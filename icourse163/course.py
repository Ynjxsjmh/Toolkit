from util import camel_to_snake


class Course(object):
    """
    'course_id': '32042'
    'gmt_create': '1080372281935'
    'gmt_modified': '1320812683935'
    'id': '3295840821'
    'member_id': '9082103'
    'mode': '0'
    'position': '0'
    'rel_type': '1'
    'term_id': '8329047283'
    """

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, camel_to_snake(key), dictionary[key])

        for key in kwargs:
            setattr(self, camel_to_snake(key), kwargs[key])
