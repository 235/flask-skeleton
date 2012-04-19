#!/bin/bash
source $(dirname $0)/venv/bin/activate
echo 'virtualenv should have been activated, running dev server'
trap "find app -name *.pyc | xargs rm" SIGINT SIGTERM EXIT

python app/manage.py runserver --config config.Dev

