# Inception example

This is an example of a system for automatically creating pipelines that was created in order to create a
video of it working, rather than as an example of good code for such a system.
It isn't intended to be used for anything real, or to be a particularly good example.
It has been deliberately kept short and simple.

# Install requirements

* `git clone https://github.com/ivanmoore/inception.git`
* [Docker](https://www.docker.com/) - [mac](http://docs.docker.com/mac/started/) [linux](http://docs.docker.com/linux/started/) [windows](http://docs.docker.com/windows/started/)
* [Docker Compose](https://docs.docker.com/compose/install/)

# Run the GoCD server and agent

* docker-compose up -d

# See GoCD server running

View [http://localhost:8153](http://localhost:8153)

* on a mac you'll need to do something special like `docker-machine ip default` to find the appropriate ip address to use instead of "localhost".

# Set up inception pipeline

* docker-compose run configure bash

Inside container just started, run: 

`./create_inception_pipeline.py`

Note that this will run a script curled from my GitHub account.
Don't run it until you have read the code and understood what it is doing.

# Trigger inception

either:

* press the "play" button on the "inception" pipeline in the GoCD UI [http://localhost:8153](http://localhost:8153)

or:

from within the container you just used for `./create_inception_pipeline.py`:

* `curl -X POST http://go-server:8153/go/api/pipelines/inception/schedule`

or:

wait up to an hour (you could reduce the poll time by changing the value passed in to `set_timer` in `create_inception_pipeline.py`.

# Create new repos

* if you are me, create a new repo in https://github.com/teamoptimization
* alternatively, clone this repo and edit value passed in to `github.get_user` in `inception.py` 

# Do something that changes pipeline

* if you are me, edit one of the "command.txt" files in one of the repos in https://github.com/teamoptimization
* alternatively, clone this repo and edit inception.py (as in *Create new repos*), then edit one of the "command.txt" files in one of the relevant repos
