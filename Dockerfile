FROM python:3.10
LABEL authors="nice"
RUN pip install --upgrade pip
COPY . /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
