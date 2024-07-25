from configparser import ConfigParser
from Config import getConfig, conf2obj, ConfigStruct

from os.path import expanduser
from pathlib import Path


class ConfMgr(object):
    """!
    """

    __fallbackPath = "templates/fallback.ini"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfMgr, cls).__new__(cls)
        return cls.instance

    def parse(self, confPath: str = None):
        """!
        """
        if confPath is None:
            print("no explicit config")
            self.__conf = conf2obj(getConfig(ConfMgr.__fallbackPath), "META")
            isConfigFound = False
            for location in self.__conf.cfgpaths.split(',\n'):
                # pass potential configs somewhere to parse
                if self.__configPathExists(location):
                    self.__parseConfFileSections(location)
                    isConfigFound = True
            if not isConfigFound:
                self.__parseConfFileSections(ConfMgr.__fallbackPath)
        else:
            self.__parseConfFileSections(confPath)

    def __

    def __configPathExists(self, path: str) -> bool:
        """!
        checks that the provided path corresponds to a real path to a real file
        @param path string representation of a path to an ini style config
        @returns bool true iff path exists else false.
        """
        if Path(expanduser(path)).is_file():
            return True
        else:
            return False

    def __parseConfFileSections(self, path: str) -> None:
        print("parsing: ", path)


class ConfigManager:
    """!
    ConfigManager provides access to config values taken from a config file in
    .ini format. by default the values contained in this object will be from a
    fallback config contained in this repo however methods are provided to:
        - locate a config file from a predefined list of places (specified in
          the fallback config).
        -
    """

    def __init__(self, fallbackOrCustom: str):
        """!
        constructs a ConfigManager object. This relies on a fallback config
        being available which provides two things:
            1. meta information about where to look for user config files.
            2. a sane set of defaults should the user not have created a config
               file of their own, in one of the places defined above.
        @param fallback a string representing the path to the fallback config
               (relative to the project root).
        @note for more details regarding the fallback config please see
              fallback_config_sanity_test.py
        """
#        self.configFile_ = fallback
#        self.parseConfig(fallback)
        self.meta = conf2obj(getConfig(fallbackOrCustom),
                             section="META")

    def getConfig(self, configFile: str = None) -> None:
        """!
        TODO - FILL THIS IN
        """
        if configFile is None:
            self.configFile_ = self.findConfigFile()
        else:
            self.configFile_ = configFile

        print("we are using: " + self.configFile_)

#        for element in self.meta.languages.split(','):
#            print(element.strip())
#
#        for element in self.meta.cfglocations.split(','):
#            print(element.strip())

#    def parseConfig(self, configFileLocation):
#        self.config = ConfigParser()
#        self.config.read(configFileLocation)
#
#        print("----")
#        print(configFileLocation)
#
#        print(self.__dict__)
#        for section in self.config.sections():
#            for item in self.config.items(section):
#                print(section, " - ", item[0], " : ", item[1])
#                self.__dict__.update()

    def findConfigFile(self) -> str:
        for location in self.meta.cfgpaths.split(','):
            location = location.strip()
            if Path(expanduser(location)).is_file():
                #need to test for lack of conf file in normal places and stay
                # stay with fallback.ini if that is the case.
                return location
