FROM ubuntu:22.04

# Metadata
LABEL name="CI PBG"
LABEL maintainer="PythonBiellaGroup"

ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y \
    libpq-dev gcc wget curl gnupg2 openssh-client make build-essential git unzip\
    && mkdir -p ~/.ssh \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Install aws cli
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && ./aws/install \
#     && rm -rf awscliv2.zip ./aws

# Setup a ssh config file
# COPY bin/ssh-config.sh /usr/bin/ssh-config.sh
# COPY ./config /root/.ssh/config
# RUN chmod 400 /root/.ssh/config
# RUN chmod +x /usr/bin/ssh-config.sh