#!/bin/bash
if [ ! -d venv_for_seaborn ] ; then
  sudo apt-get install python3-venv
  python3 -m venv $(dirname $0)/venv_for_seaborn
  . venv_for_seaborn/bin/activate
  pip install --upgrade pip
  pip install --upgrade setuptools
  pip install seaborn
fi
. venv_for_seaborn/bin/activate
