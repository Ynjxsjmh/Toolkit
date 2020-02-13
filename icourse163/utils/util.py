# -*- coding: utf-8 -*-
import json
import inflection


# https://stackoverflow.com/questions/16058065
def raw_unicode_escape(string: str) -> str:
    return json.loads('{}'.format(string))


def camel_to_snake(name: str) -> str:
    return inflection.underscore(name)
