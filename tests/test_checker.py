from siteonlinechecker.loader import config, data
from siteonlinechecker.checker import Checker

def test_checker():
    checker = Checker()
    config.set('default', 'keyword', 'baidu')
    assert checker.check('http://www.baidu.com') == True
    assert checker.check('http://www.163.net') == False
    assert checker.check('http://unknown.richardma.info') == False
