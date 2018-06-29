FROM arm32v6/python:2.7-alpine3.7


RUN apk add --no-cache  build-base

WORKDIR /home
RUN  pip install gpiozero && pip install RPi.GPIO


ENTRYPOINT ["python"]
