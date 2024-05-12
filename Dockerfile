FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_VERSION=1.7.1

RUN apt update && apt-get install -y libcublas-12-0

RUN apt update && \
    apt -y install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt -y install python3.11 python3-pip python3.11-dev python3.11-distutils curl && \
    apt-get install -y cmake pkg-config git && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN python3.11 -m pip3 install --no-cache-dir poetry==${POETRY_VERSION} && \
    poetry config virtualenvs.create false

RUN poetry install --only=main --no-root --no-interaction --no-cache

COPY . .

CMD ["python3", "src/start.py"]

