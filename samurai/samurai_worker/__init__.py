from celery import current_app

from samurai.samurai_utils import config

def create_worker():
    settings = config.get_settings()
    celery_app = current_app
    celery_app.config_from_object(settings)

    return celery_app
