FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /src
ADD . /src

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["server.py"]