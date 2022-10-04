#!/bin/sh

celery -A samurai.main.celery worker -E --loglevel=INFO --concurrency=10 -n worker@%h