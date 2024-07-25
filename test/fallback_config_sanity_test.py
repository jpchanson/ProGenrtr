from configparser import ConfigParser
from os.path import exists
from pathlib import Path

import pytest

fallbackConf = "templates/fallback.ini"
configPathSection = "META_CONFIG_PATHS"

def test_fallback_config_exists():
    """!
    @test that the fallback config specified exists
    """
    assert Path(fallbackConf).is_file()

def test_fallback_has_meta_config_paths_section():
    """
    @test The fallback config file MUST contain a section called META_CONFIG_PATHS
    """
    fallback = ConfigParser()
    fallback.read(fallbackConf)
    assert fallback.has_section(configPathSection)


def test_fallback_config_paths_not_empty():
    """
    @test the META_CONFIG_PATHS section is not empty.
    """
    fallback = ConfigParser()
    fallback.read(fallbackConf)
    assert len(fallback.items(configPathSection)) > 0
