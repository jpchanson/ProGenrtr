import pytest

from ConfigManager import ConfigManager
from Config import getConfig, conf2obj

test_fallbackConf = "test/resources/fallback.ini"
configPathsSection = "META_CONFIG_PATHS"


def test_fallback_is_successfully_parsed():
    confMgr = ConfigManager(test_fallbackConf)
    assert confMgr.config.has_section(configPathsSection)


def test_fallback_contains_necessary_config():
    TEST = conf2obj(getConfig(test_fallbackConf), section="META_CONFIG_PATHS")
    assert TEST.cfgprimary == "~/.progenrtr.conf"
    assert TEST.cfgsecondary == "~/.config/progenrtr/progenrtr.conf"
    assert TEST.cfgglobal == "/etc/progenrtr.conf"
