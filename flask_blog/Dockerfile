
FROM centos:latest

#Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel
RUN easy_install pip
RUN mkdir /opt/flask_blog
WORKDIR /opt/flask_blog
ADD requirements.txt /opt/flask_blog/
RUN pip install -r requirements.txt
ADD . /opt/flask_blog
