FROM --platform=linux/amd64 postgres:16.8

RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y libpq-dev gcc curl

RUN mkdir -p /project/backup/
RUN mkdir -p /project/query/

# Automatically initialize and configure the database
# COPY scripts/init.sql /docker-entrypoint-initdb.d/

# Automatically initialize backups
#COPY backup/backup.sql /project/backup/

# install python

# launch postgres
CMD ["postgres"]
