# -*- coding: utf-8 -*-
import json
import inflection
from statistics import mode, StatisticsError


# https://stackoverflow.com/questions/16058065
def raw_unicode_escape(string: str) -> str:
    return json.loads('{}'.format(string))


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
