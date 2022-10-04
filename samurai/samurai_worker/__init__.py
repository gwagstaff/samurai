from celery import current_app

from samurai.samurai_utils import config

def create_worker():
    settings = config.get_settings()
    celery_app = current_app
    celery_app.config_from_object(settings)
    celery_app.autodiscover_tasks(packages=['samurai.samurai_worker.units'], force=True)
    return celery_app
