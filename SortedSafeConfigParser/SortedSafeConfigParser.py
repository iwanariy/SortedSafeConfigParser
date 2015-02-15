# coding: utf-8

from ConfigParser import SafeConfigParser


DEFAULTSECT = "DEFAULT"


class SortedSafeConfigParser(SafeConfigParser):
    def write(self, fp, sort=False):
        """Override write()"""
        if self._defaults:
            fp.write("[%s]\n" % DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s = %s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        if sort:
            for section in sorted(self._sections.keys()):
                fp.write("[%s]\n" % section)
                for key in sorted(self._sections[section].keys()):
                    value = self.get(section, key)
                    if key == "__name__":
                        continue
                    if (value is not None) or (self._optcre == self.OPTCRE):
                        key = " = ".join((key, str(value).replace('\n', '\n\t')))
                    fp.write("%s\n" % (key))
                fp.write("\n")
        else:
            for section in self._sections:
                fp.write("[%s]\n" % section)
                for (key, value) in self._sections[section].items():
                    if key == "__name__":
                        continue
                    if (value is not None) or (self._optcre == self.OPTCRE):
                        key = " = ".join((key, str(value).replace('\n', '\n\t')))
                    fp.write("%s\n" % (key))
                fp.write("\n")
