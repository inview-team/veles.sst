FROM nvidia/cuda:12.3.2-devel-ubuntu20.04

RUN apt update -y && apt-get install -y python3 python3-pip libcublas-12-0 libcudnn8 libcudnn8-dev

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /app/src

CMD ["python3", "start.py"]

