FROM --platform=linux/amd64 python:3.9-slim-buster as python

# Metadata
LABEL name="PBG Bear"
LABEL maintainer="PBG"
LABEL version="0.1"

ARG YOUR_ENV="virtualenv"
ARG POETRY_VERSION=1.6.1

ARG DEBIAN_FRONTEND=noninteractive

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION} \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

ENV PATH="$POETRY_HOME/bin:$PATH"

# add ssh config capabilities
# RUN mkdir -p ~/.ssh
# COPY bin/ssh-config.sh /usr/bin
# RUN chmod +x /usr/bin/ssh-config.sh

# Install libraries
RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y \
    libpq-dev gcc wget gnupg2 curl openssh-client git make build-essential \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# # add custom host file for your services
# COPY hosts tmp/
# ADD hosts /tmp/hosts
# # Warning: if you test on M1 and arch64 architecture you could have an issue with this line
# RUN mkdir -p -- /lib-override && cp /lib/x86_64-linux-gnu/libnss_files.so.2 /lib-override
# # If you are using mac or arch64 change X86_64-linux-gnu with aarch64-linux-gnu
# RUN perl -pi -e 's:/etc/hosts:/tmp/hosts:g' /lib-override/libnss_files.so.2
# ENV LD_LIBRARY_PATH /lib-override

RUN  wget -O install-poetry.py https://install.python-poetry.org/ \
    && python3 install-poetry.py --version ${POETRY_VERSION}

# Install Node
#RUN apt-get update && apt-get install -y curl && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs

# Copy ssh keys from local machine to dev container
#RUN ssh-add $HOME/.ssh/keyname

WORKDIR /workspace

#Copy all the project files
COPY . .

# Install libraries
RUN poetry install