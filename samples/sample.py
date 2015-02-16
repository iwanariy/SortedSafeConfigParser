# coding: utf-8

from SortedSafeConfigParser import SortedSafeConfigParser
import ConfigParser


INI_FILE = 'input/sample.ini'
OUT_DIR = 'output/'


if __name__ == '__main__':
    # Original
    config = ConfigParser.ConfigParser()
    config.read(INI_FILE)
    with open(OUT_DIR + 'result_org.ini', 'w') as f:
        config.write(f)

    # SortedSafeConfigParser
    sorted_config = SortedSafeConfigParser.SortedSafeConfigParser()
    sorted_config.read(INI_FILE)
    with open(OUT_DIR + 'result_sorted.ini', 'w') as f:
        sorted_config.write(f, sort=True)
