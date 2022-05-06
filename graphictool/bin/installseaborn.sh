#!/bin/bash
if [ ! -d venv_for_seaborn ] ; then
  sudo apt-get install python3-venv
  python3 -m venv $(dirname $0)/venv_for_seaborn
  . venv_for_seaborn/bin/activate
  pip3 install --upgrade pip
  pip3 install --upgrade setuptools
  pip3 install seaborn
fi
. venv_for_seaborn/bin/activate
