FROM python:latest
LABEL version=1.0.0
WORKDIR /app
RUN apt-get update
ENV DATE 07-07-2019
ADD ./requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV ENVIRONMENT test
ENTRYPOINT ["python", "manage.py", "runserver"]
