#Python3 parent image
FROM python:3.6

#File Author/Maintainer
MAINTAINER Johann Jesse

#Ensure that Python outputs all log messages inside the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/projects/compfinal

# specify the working dir inside the container
WORKDIR /var/projects/compfinal

ADD requirements.txt /var/projects/compfinal

#install requirements from txt file
RUN pip install --no-cache-dir -r requirements.txt

# add current dir's content to container's WORKDIR root i.e. all the contents of the web app
ADD . /var/projects/compfinal

#Expose port 8000 on docker virtual network
EXPOSE 8000
