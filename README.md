flask-skeleton
==============

This skeleton is an empty web project based on python web micro framework [Flask](http://flask.pocoo.org/). It also based on [Diesel](http://diesel.io/) network framework which gives nonblocking I/O, but this dependence can be easily turned on/off by altering lines commented as #FallBackToFlask. 
By bootstraping with this skeleton you will be able to start moking up a new index page as soon as it possible. It meant to be used under Linux (possibly MacOS).

The skeleton uses the most recent versions of the frameworks from github. It was tested with the following versions: 
  - Flask 0.9-dev
  - Flask-Script 0.3.4
  - Diesel 3.0b1

There are a number of other flask-skeletons on github and you are welcome to compare them. However, I personally found some issues with many of them (such as being outdated, too sophisticated for a bootstrap etc.) and putting here my compilation. Still, many of them gave me ideas and initially I was inspired by:
  - [flask-empty](https://github.com/italomaia/flask-empty)

How to Start
------------
  - execute *bootstrap_venv.sh* to automatically install all dependencies into a python virtualevn
  - run dev-server with *rundev.sh*. To enter virtualenv for other actions type *source venv/bin/activate* in your console (assuming you are using bash).
  - open *http://localhost:8080/* in your browser, you'll get a dummy index page. 
  - go and hack the skeleton
