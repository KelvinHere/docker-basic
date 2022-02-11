# Simple Example of Docker

This docker image when built will contain a Python program that uses Numpy to generate a random number (as a purposeful dependency).


## Dockerfile contents
* ```FROM python:3.8``` # Uses the default python 3.8 image from docker images

* ```ADD main.py .``` # Files to add to this image

* ```RUN pip install numpy``` # List of dependencies to add to image

* ```CMD [ "python", "./main.py" ]``` # Default execution point for container

## Steps to use

1. Clone repo to local machine

1. ```docker build -t python-numpy``` from working directory, build the docker image named python-numpy

1. ```docker run -ti python-numpy``` runs the created image in a docker container in interactive mode (-i) with terminal (-t)

