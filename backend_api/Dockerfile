FROM python:3-alpine3.8

WORKDIR /usr/src

COPY requirements.txt .

RUN pip install --upgrade pip

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    ; \
    pip install -r requirements.txt; \
    apk del .build-deps;

COPY . .

RUN pip install -e .

CMD ["uwsgi", "--ini-paste", "service_api/config/config_files/development.ini"]
