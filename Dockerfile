FROM ubuntu
MAINTAINER archana.nagaraj@gmail.com
RUN apt-get upgrade && apt-get update && apt-get install -y python3
COPY app.py  opt/app.py
CMD echo "from dockerfile"
CMD flask run
