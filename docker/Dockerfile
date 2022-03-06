
FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

SHELL ["/bin/bash", "-c"]

WORKDIR /tmp

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y less unzip libmagic-dev

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python3 -m spacy download en

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app
