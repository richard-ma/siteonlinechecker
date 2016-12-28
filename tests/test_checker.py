from siteonlinechecker.loader import config, data
from siteonlinechecker.checker import Checker

def test_checker_check():
    checker = Checker()
    config.set('default', 'keyword', 'baidu')
    assert checker.check('http://www.baidu.com') == True
    assert checker.check('http://www.163.net') == False
    assert checker.check('http://unknown.richardma.info') == False

def test_checker_checkCases():
    data = ['http://www.baidu.com',
            'http://www.163.net',
            'http://unknown.richardma.info']
    checker = Checker()
    config.set('default', 'keyword', 'baidu')
    failed_cases = checker.checkCases(data)
    assert len(failed_cases) == 2
    assert not ('http://www.baidu.com' in failed_cases)
    assert 'http://www.163.net' in failed_cases
    assert 'http://unknown.richardma.info' in failed_cases
