#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM centos:latest

# Build commands
RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y update
RUN yum -y install python-pip
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel
RUN mkdir /opt/flask_blog
WORKDIR /opt/flask_blog
ADD requirements.txt /opt/flask_blog/
RUN pip install -r requirements.txt
ADD . /opt/flask_blog

# Define working directory.
WORKDIR /opt/flask_blog


EXPOSE 5000

