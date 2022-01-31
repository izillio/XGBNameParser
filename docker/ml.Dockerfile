FROM ubuntu:18.04

# Basic toolchain
RUN apt-get update && apt-get install -y \
        apt-utils \
        build-essential \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        zlib1g-dev

# ENV Variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION="3.6.5"

# Install Python 3.6.5
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz \
    && tar xvf Python-${PYTHON_VERSION}.tar.xz \
    && rm Python-${PYTHON_VERSION}.tar.xz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure \
    && make altinstall \
    && cd / \
    && rm -rf Python-${PYTHON_VERSION}

RUN apt-get update && apt-get install -y \
                       libcurl4-openssl-dev \
                            zlib1g-dev \
                            htop \
                            cmake \
                            nano \
                            python3-pip \
                            python3-dev \
                            python3-tk \
                            libx264-dev \
                            ca-certificates \
                            gcc \
                            g++ \
                        && cd /usr/local/bin \
                        && ln -s /usr/bin/python3 python \
                        && pip3 install --upgrade pip \
                        && apt-get autoremove -y

CMD set PYTHONIOENCODING=utf-8

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

ADD ./docker /docker
RUN pip3 install -r /docker/requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

