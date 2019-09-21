FROM ubuntu:16.04

ENV LC_ALL=C.UTF-8

# Gather all needed dependencies and 
# install yle-dl and add it to PATH
RUN apt-get update && apt-get install -y git rtmpdump wget ffmpeg python3-dev python3-setuptools \
    python3-pip python3-crypto python3-requests python3-lxml \
    php-cli php-curl php-xml php-bcmath && \
    git clone https://github.com/aajanki/yle-dl.git && \
    apt-get purge -y --auto-remove git && \ 
    rm -rf /var/lib/apt/lists/*

WORKDIR /yle-dl/
RUN python3 setup.py install --user

ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /out

ENTRYPOINT [ "yle-dl" ]