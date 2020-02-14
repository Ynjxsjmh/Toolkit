# -*- coding: utf-8 -*-
import json
import inflection
import traceback
from statistics import mode, StatisticsError


# https://stackoverflow.com/questions/16058065
def raw_unicode_escape(string: str) -> str:
    """
    'name': '"\\u9AD8\\u7EA7\\u8BED"',
    'imgUrl': '"http://edu-im"'
    1. 将 name 转化为中文
    2. 将两个字符串一起的转成一个字符串
    """
    result = ""
    try:
        result = json.loads('{}'.format(string))
    except AttributeError:
        try:
            result = json.loads('"{}"'.format(string))
        except AttributeError:
            traceback.print_exc()
    return result


def camel_to_snake(name: str) -> str:
    return inflection.underscore(name)


def most_common(l):
    try:
        return mode(l)
    except StatisticsError as e:
        # will only return the first element if no unique mode found
        if 'no unique mode' in e.args[0]:
            return l[0]
        # this is for "StatisticsError: no mode for empty data"
        # after calling mode([])
        raise
