#!/usr/bin/python3
# coding: utf-8

from sys import argv
from os import mkdir
from os import system
from os.path import exists
from os.path import dirname
from os.path import realpath
from configparser import ConfigParser


class Main:
    def __init__(self):
        self.basedir = dirname(realpath(__file__))
        self.config = ConfigParser()
        self.config.read(self.basedir + "/conf/hor.conf", "utf-8")
        self.config_sections = self.config.sections()
        self.scan_dir = "/mnt"
        self.move_dir = self.basedir + "/infected_files"
        self.remove_files = "no"
        self.mail_subject = ""
        self.mail_admin = ""
        self.servername = "Servidor"
        self.mutt_file = self.basedir + "/conf/muttrc"

    def run(self):
        parameter = ""
        try:
            parameter = argv[1]
        except IndexError:
            pass

        if not exists(self.move_dir):
            mkdir(self.move_dir)

        path_exists = exists(parameter)
        if path_exists:
            cmd = """
            clamscan -r {0} \
            --exclude-dir=/sys \
            --exclude-dir={1} \
            --move={1} \
            --remove=yes
            """
            system(cmd.format(parameter, self.move_dir))
        else:
            for section in self.config_sections:
                self.servername = self.config.get(section, 'hostname')
                self.scan_dir = self.config.get(section, 'scan_dir')
                self.mail_subject = self.config.get(section, 'mail_subject')
                self.mail_subject = self.mail_subject \
                    + " | " + self.servername + " - " + section
                self.mail_admin = self.config.get(section, 'mail_admin')
                self.remove_files = self.config.get(section, 'remove_files')

                if not exists(self.move_dir):
                    mkdir(self.move_dir)
                command = """
                clamscan -ri {0} \
                --exclude-dir=/sys \
                --exclude-dir={1} \
                --move={1} \
                --remove={2} \
                |mutt -F {3} -s '{4}' {5}
                        """
                system(command.format(
                    self.scan_dir,
                    self.move_dir,
                    self.remove_files,
                    self.mutt_file,
                    self.mail_subject,
                    self.mail_admin
                    )
                )
            else:
                if len(self.config_sections) == 0:
                    print("Não há seções configuradas")
                else:
                    print("Fim da execução!")


if __name__ == "__main__":
    app = Main()
    app.run()
