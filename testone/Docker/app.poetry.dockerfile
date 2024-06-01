FROM --platform=linux/amd64 python:3.9-slim-buster as python

# Metadata
LABEL name="PBG Bear"
LABEL maintainer="PBG"
LABEL version="0.1"

ARG YOUR_ENV="virtualenv"
ARG POETRY_VERSION="1.6.1"

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
    && python install-poetry.py --version ${POETRY_VERSION}

# Project Python definition
WORKDIR /app

#Copy all the project files
COPY pyproject.toml .
COPY poetry.lock .
COPY poetry.toml .

RUN poetry install --no-interaction --no-ansi --only main && \
    rm -rf /root/.cache/pypoetry
RUN poetry cache clear --all pypi

COPY /app ./app
COPY .env .
COPY ./scripts/launch.sh .
# COPY docs ./docs
# COPY mkdocs.yml .

#Launch the main (if required)
RUN chmod +x launch.sh
CMD ["bash", "launch.sh"]

#if you want to test the image
# CMD ["tail", "-f", "/dev/null"]
