import requests
import re

from loader import config, data

class Checker(object):

    def __init__(self):
        pass

    def check(self, target):
        try:
            r = requests.get(target)
            # unfound keyword
            if r.text.find(config.get('default', 'keyword')) == -1:
                raise requests.exceptions.RequestException()
        except requests.exceptions.RequestException:
            return False
        else:
            return True
