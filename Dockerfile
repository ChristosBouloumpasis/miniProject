FROM ubuntu:19.04

COPY . /app

RUN apt-get update \
	&& apt-get install -y python3 python3-pip python3-dev \
	&& pip3 install --upgrade pip


RUN pip3 install -r app/requirements.txt

EXPOSE 8088

ENTRYPOINT ["python3","app/flask_website.py"]