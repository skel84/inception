#!/bin/bash

# for building images and pushing to docker hub

docker build -t ivanmoore/inception-configure configure
docker push ivanmoore/inception-configure

docker build -t ivanmoore/inception-agent gocd-agent
docker push ivanmoore/inception-agent