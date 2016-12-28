import ConfigParser

class Config(object):

    def __init__(self):
        self.config = None

    def load(self, configFilename = '../config.cfg'):
        cp = ConfigParser.ConfigParser()
        self.config = cp.read(configFilename)
        return self.config
