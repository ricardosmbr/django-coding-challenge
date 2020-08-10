FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /appi
WORKDIR /appi
COPY requirements.txt /appi/
RUN pip install -r requirements.txt
COPY . /appi/
