FROM --platform=linux/amd64 python:3.12-slim

WORKDIR /app

# Copy only the necessary files
COPY pyproject.toml poetry.lock ./
COPY src/ ./src/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install git -y

RUN pip3 install poetry==1.8.4

RUN poetry config virtualenvs.in-project true

RUN poetry export --only main --without-hashes --output /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

# Add PYTHONPATH to ensure src is in the Python path
ENV PYTHONPATH=/app

CMD [ "python", "src/main.py"]
