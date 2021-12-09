ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN apt-get update \
  && apt-get -y install vim

ARG POETRY_VERSION="1.0"
COPY poetry.lock pyproject.toml ./
RUN pip install "poetry~=$POETRY_VERSION" \
  && poetry config virtualenvs.create false \
  && poetry install
