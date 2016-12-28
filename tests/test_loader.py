import pytest

from siteonlinechecker import loader

def test_config_loader():
    c = loader.Config()
    c.load()
    assert c != None
