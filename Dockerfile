#This is a sample Image
FROM ubuntu
MAINTAINER test@gmail.com

RUN apt-get update
RUN apt-get upgrade -y
RUN apt install python3 -y
RUN apt install pip -y
RUN mkdir -p app
RUN pip install boto3

ADD . /app/
WORKDIR /app/
CMD ./install.sh
RUN ./env.sh
CMD ["python3" , "/app/sms_module/main.py"]