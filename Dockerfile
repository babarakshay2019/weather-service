# base image
FROM python:3.8

#maintainer
LABEL Author="CodeGenes"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app sourcdocker-compose run zuri django-admin startproject zuri .e code
RUN mkdir /weather_service

#switch to /app directory so that everything runs from here
WORKDIR /weather_service

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#copy the app code to image working directory
COPY ./ ../weather_service

#let pip install required packages
RUN pip install -r requirements.txt