#!/bin/sh

celery -A samurai.main.celery worker -E