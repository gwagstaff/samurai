###############################################
# Builder Image
###############################################
ARG TARGETPLATFORM
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.9-buster AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry export --output /requirements.txt

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /requirements.txt


###############################################
# Base Image
###############################################
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.9-slim-buster AS python-base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

# Add non root user
RUN addgroup --system app && adduser app --system --ingroup app

WORKDIR /home/app

# Copy over project files
COPY --from=builder /wheels/                ./wheels/
COPY --from=builder /requirements.txt       ./requirements.txt
COPY samurai/                               ./samurai/
COPY build/                                 /
RUN chown -R app /home/app && mkdir -p /home/app/python && chown -R app /home/app

USER app

# Install previously built python wheels
RUN pip install --no-cache /home/app/wheels/* --target=/home/app/python

###############################################
# API Image
###############################################
FROM python-base as samurai-api

HEALTHCHECK --start-period=30s CMD python -c "import requests; requests.get('http://localhost:8000', timeout=2)"

EXPOSE 8000

CMD ["/api-start.sh"]

###############################################
# Worker Image
###############################################
FROM python-base as samurai-worker

CMD ["/worker-start.sh"]