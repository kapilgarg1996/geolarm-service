FROM python:latest
LABEL version=1.0.0
WORKDIR /app
RUN apt-get update
ENV DATE "13-07-2019 19:25"
ADD ./requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV ENVIRONMENT test
CMD ["python", "manage.py", "runserver", "0:80"]
