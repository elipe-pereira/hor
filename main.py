#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from configparser import ConfigParser

class Main:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.config = ConfigParser()
        self.config.read(self.base_dir + "config/hor.conf")
        self.config_sections = self.config.sections()
        self.scan_dir = "/mnt"
        self.move_dir = self.base_dir + "/infected_files"
        self.remove_files = "no"
        self.mail_admin = ""


    def run(self):
        for section in self.config_sections:
            if section == "DEFAULT":
                continue
            else:
                self.scan_dir = self.config.get(section, 'scan_dir')
                self.mail_admin = self.config.get(section, 'mail_admin')
                self.remove_files = self.conf.get(section, 'remove_files')

                if not os.path.exists(self.move_dir):
                    os.mkdir(self.move_dir)

                os.system("clamscan -r {0} --move={1} --remove={2}".format(self.scan_dir,
                                                                           self.move_dir,
                                                                            self._remove_files
                                                                           ))


if __name__ == "__main__":
    app = Main()
    app.run()
