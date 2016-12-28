import requests

from loader import config, data

class Checker(object):

    def __init__(self):
        self.failed_cases = list()

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

    def checkCases(self, data):
        for target in data:
            if self.check(target) == False:
                self.failed_cases.append(target)

        return self.failed_cases
