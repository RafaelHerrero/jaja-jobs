FROM --platform=linux/amd64 python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install git -y

COPY . /app/apps/

RUN pip3 install poetry==1.8.4

RUN poetry config virtualenvs.in-project true

RUN poetry export --only main --without-hashes --output /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 80

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
