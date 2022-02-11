# Simple Example of Docker

Python program uses Numpy to generate a random number


## Dockerfile contents
* ```FROM python:3.8``` # Uses the default python 3.8 image from docker images

* ```ADD main.py .``` # Files to add to this image

* ```RUN pip install numpy``` # List of dependancies to add to image

* ```CMD [ "python", "./main.py" ]``` # Default execution point for conatiner

## Commands

* ```docker build -t python-numpy``` builds the docker image named python-numpy, add -ti for ineractive terminal, ie user input

* ```docker run python-numpy``` runs the created image in a docker container