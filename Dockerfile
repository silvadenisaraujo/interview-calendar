FROM ubuntu:latest
MAINTAINER Denis Silva "silvadenisaraujo@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["manage.py db init"]
CMD ["manage.py db migrate"]
CMD ["manage.py db upgrade"]
CMD ["run.py"]
