import ConfigParser

def remove_newline(e):
    return e.strip()

class Config(object):

    def __init__(self):
        self.config = None

    def load(self, configFilename):
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(configFilename)
        return self.config

class Data(list):
    def __init__(self, dataFilename):
        super(Data, self).__init__()

        with open(dataFilename) as f:
            self.extend(list(map(remove_newline, f.readlines())))

# global config object
config = Config().load('config.cfg')
data = Data(config.get('default', 'targets_file'))

if __name__ == '__main__':
    pass
