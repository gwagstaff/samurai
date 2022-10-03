import logging
from fastapi import FastAPI, BackgroundTasks

from samurai.samurai_utils import config

log = logging.getLogger(__name__)
settings = config.get_settings()

def background_on_message(task):
    log.warning(task.get(on_message=celery_on_message, propagate=False))

def celery_on_message(body):
    log.warning(body)
