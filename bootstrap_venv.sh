#!/bin/bash
sudo easy_install pip virtualenv
virtualenv --no-site-packages ./venv
source venv/bin/activate

function githubinstall {
  echo '========= Installing the latest ' $1
  git clone --depth 1 $1 ./tmp
  pip install ./tmp
  echo '========= Cleaning'
  rm -f -r tmp
}

githubinstall https://github.com/jamwt/diesel
#githubinstall https://github.com/mitsuhiko/flask/
#githubinstall https://github.com/rduplain/flask-script

#======== Process pip-requirements
pip install -r requirements.txt
