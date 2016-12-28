import ConfigParser
from siteonlinechecker.loader import config, data

def test_load_config():
    # load completed?
    assert isinstance(config, ConfigParser.ConfigParser)

    # default section options
    assert config.has_section('default')
    assert config.has_option('default', 'keyword')
    assert not(config.get('default', 'keyword') is None)

    # smtp section options
    assert config.has_section('smtp')
    assert config.has_option('smtp', 'host')
    assert config.has_option('smtp', 'username')
    assert config.has_option('smtp', 'password')
    assert config.has_option('smtp', 'port')
    assert not(config.get('smtp', 'host') is None)
    assert not(config.get('smtp', 'username') is None)
    assert not(config.get('smtp', 'password') is None)
    assert not(config.get('smtp', 'port') is None)

def test_load_data():
    assert isinstance(data, list)
