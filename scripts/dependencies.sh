#!/bin/bash
# dependencies.sh -
# script faz a instalação dos pacotes que
# o hor usa para scanear o sistema operacional linux.
apt-get install clamav -y
apt-get install mutt -y
# Atualiza a base de dados do clamav
freshclam