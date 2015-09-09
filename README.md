# Inception example

This is an example of a system for automatically creating pipelines that was created in order to create a
video of it working, rather than as an example of good code for such a system.
It isn't intended to be used for anything real, or to be a particularly good example.
It has been deliberately kept short and simple.

# Install requirements

* [Docker](https://www.docker.com/) - [mac](http://docs.docker.com/mac/started/) [linux](http://docs.docker.com/linux/started/) [windows](http://docs.docker.com/windows/started/)
* [Docker Compose](https://docs.docker.com/compose/install/)

# Run the GoCD server and agent

* docker-compose up -d

# See GoCD server running

View [http://localhost:8153](http://localhost:8153)

# Set up inception pipeline

* docker-compose run configure bash

Inside container just started, run: 

`./create_inception_pipeline.py`

Note that this will run a script curled from my GitHub account.
Don't run it until you have read the code and understood what it is doing.

# Create new repos

* if you are me, create a new repo in https://github.com/teamoptimization
* alternatively, clone this repo and edit inception.py line 5 

# Do something that changes pipeline

* if you are me, edit one of the "command.txt" files in one of the repos in https://github.com/teamoptimization
* alternatively, clone this repo and edit inception.py line 5, then edit one of the "command.txt" files in one of the relevant repos
