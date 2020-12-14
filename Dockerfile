FROM python:3.9-alpine

WORKDIR /src
ADD . /src

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["server.py"]