import pytest

from siteonlinechecker import config

def test_load():
    c = config.Config()
    c.load()
    assert c != None
