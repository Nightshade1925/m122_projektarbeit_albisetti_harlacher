# GITTOOLS 


## [git_gengraphics.py](bin/git_gengraphics.py)

### Usage

If you run it the first time and have never run the [installseaborn.sh](bin/installseaborn.sh) script before you should run this first.
The install script should work on Debian and Ubuntu VMs as they use apt.
This script installs the seaborn library with all its dependencies in a virtual env. Best is to source it.
Like this you get the 
```
. ./installseaborn.sh
```
This also activates the virtual env installed in bin/venv_for_seaborn by executing:
```commandline
. bin/venv_for_seaborn/bin/activate
```
Then just run the script as explained in the usage below:
```
usage: git_gengraphics.py [-h] --csvfile CSVFILE --outputfile OUTPUTFILE

This is a script which generates from a csv file containing commits, which was
generated by git_ectract_commits.bash a stripplot graphic.

optional arguments:
  -h, --help            show this help message and exit
  --csvfile CSVFILE, -c CSVFILE
                        Commaseparated file with commits
  --outputfile OUTPUTFILE, -o OUTPUTFILE
                        Filename of outputfile for png
```
