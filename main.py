#!/usr/bin/env python3
# coding: utf-8

import os
from configparser import ConfigParser


class Main:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.config = ConfigParser()
        self.config.read(self.base_dir + "/conf/hor.conf", "utf-8")
        self.config_sections = self.config.sections()
        self.scan_dir = "/mnt"
        self.move_dir = self.base_dir + "/infected_files"
        self.remove_files = "no"
        self.mail_subject = ""
        self.mail_admin = ""
        self.servername = "Servidor"
        self.mutt_file = self.base_dir + "/conf/muttrc"

    def run(self):
        for section in self.config_sections:
            self.servername = self.conf.get(section, 'servername')
            self.scan_dir = self.config.get(section, 'scan_dir')
            self.mail_subject = self.config.get(section, 'mail_subject')
            self.mail_subject = self.mail_subject \
                + " | " + self.servername + " - " + section
            self.mail_admin = self.config.get(section, 'mail_admin')
            self.remove_files = self.config.get(section, 'remove_files')

            if not os.path.exists(self.move_dir):
                os.mkdir(self.move_dir)
            command = """
            clamscan -ri {0} \
            --exclude-dir=/sys \
            --move={1} \
            --remove={2} \
            |mutt -F {3} -s '{4}' {5}
                    """
            os.system(command.format(self.scan_dir,
                                     self.move_dir,
                                     self.remove_files,
                                     self.mutt_file,
                                     self.mail_subject,
                                     self.mail_admin
                                     ))
        else:
            if len(self.config_sections) == 0:
                print("Não há seções configuradas")
            else:
                print("Fim da execução!")


if __name__ == "__main__":
    app = Main()
    app.run()
