import configparser

FALLBACK_CONFIG = "templates/fallback.ini"


class ConfigStruct:
    """!
    data object to access config in a sane manner, essentially a dictionary
    that allows access to its keys as data members.
    """

    def __init__(self, **entries):
        self.__dict__.update(entries)


def getConfig(path: str):
    """!
    read the config file and rreturn the object return the object as parsed by
    ConfigParser.
    @param path is the path to the ini style config file
    @returns parsed config object
    """
    data = configparser.ConfigParser()
    data._interpolation = configparser.ExtendedInterpolation()
    data.read(path)
    return data


def conf2obj(data: dict, section=None):
    """!
    create a ConfigStruct from a parsed config object, either for the file as
    a whole or for a specific section of the config file.
    @param data the dictionary containing the parsed config
    @param section the section you wish to convert (optional)
    @returns ConfigStruct containg the parsed config values.
    """
    if section is None:
        return ConfigStruct(**data)
    else:
        return ConfigStruct(**data[section])
