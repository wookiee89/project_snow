FROM python:3.11.3-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y netcat curl git make gcc postgresql python3-dev libpq-dev \
    && apt-get clean

RUN pip install -U pip \
    pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
WORKDIR /app

RUN poetry install --no-interaction --no-ansi --no-root

COPY . /app

EXPOSE 8000

RUN chmod 777 scripts/run.sh

CMD ["/bin/bash", "scripts/run.sh"]