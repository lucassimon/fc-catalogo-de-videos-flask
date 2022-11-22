## base image
FROM python:3.10-alpine AS base

RUN apk --no-cache update && \
    apk add ca-certificates && \
    rm -rf /var/cache/apk/*

FROM base as dev

RUN python3 -m venv /opt/venc
ENV PATH="$VIRTUAL_ENV/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## install dependencies
RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add build-base && \
    apk add gcc && \
    apk add python3-dev && \
    apk add libffi-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk del build-base && \
    rm -rf /var/cache/apk/*
WORKDIR /app

FROM dev as ci
WORKDIR /app
## add and install requirements
RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install --upgrade pip \
    && pip install -r requirements/dev.txt


FROM ci as build
WORKDIR /app
RUN rm -rf /opt/venv && python3 -m venv /opt/venv \
    && pip install --upgrade pip \
    && pip install -r requirements/prod.txt


FROM base
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY --chown=nobody --from=build /opt/venv /opt/venv
COPY --chown=nobody --from=build /app /app
USER nobody

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["gunicorn", "--config", "gunicorn_settings.py", "-b", "0.0.0.0:8000", "run:app"]
