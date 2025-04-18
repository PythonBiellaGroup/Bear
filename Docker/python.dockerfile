# Reference:
# * https://hynek.me/articles/docker-uv/

ARG UV_VERSION="0.6.14"
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM python:3.12-slim AS base

# Metadata
LABEL name="Python 3.12"
LABEL maintainer="PythonBiellaGroup"

ARG UV_PYTHON=python3.12

# Install requirements and clean up
RUN apt update && apt install -y --no-install-recommends \
    curl ca-certificates libpq-dev gcc git make unzip \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Install aws cli and clean up
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && ./aws/install \
#     && rm -rf awscliv2.zip ./aws

### Start build prep

COPY --from=uv /uv /bin/uv

# - Silence uv complaining about not being able to use hard links,
# - tell uv to byte-compile packages for faster application startups,
# - prevent uv from accidentally downloading isolated Python builds,
# - pick a Python version to use for the uv command.
# - add the cargo binary directory to the PATH
ENV \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=${UV_PYTHON} \
    PATH="/root/.cargo/bin/:$PATH"

