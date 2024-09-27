FROM amd64/python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y \
        git gcc g++ make curl gettext wget \
        libxml2-dev libxslt1-dev zlib1g-dev \
        mariadb-client libmariadb-dev \
        libjpeg-dev debconf-utils pkg-config && \
    curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g sass postcss-cli postcss autoprefixer
RUN pip3 install pymysql mysqlclient websocket-client uwsgi django-redis redis

WORKDIR /
COPY repo/requirements.txt .
COPY repo/additional_requirements.txt .
COPY repo/package.json .
COPY repo/package-lock.json .
RUN npm install && \
    pip3 install -r requirements.txt && \
    pip3 install -r additional_requirements.txt
