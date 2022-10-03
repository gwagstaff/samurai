import os
import pathlib
from pydantic import (
    BaseSettings,
    RedisDsn,
    AmqpDsn,
)
from functools import lru_cache

# https://www.geeksforgeeks.org/python-functools-lru_cache/
@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
        "testing": TestingSettings
    }

    config_name = os.environ.get("DEPLOY_ENV", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


class Settings(BaseSettings):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
    app_name: str = "samurai"

    # Celery Settings
    result_backend: RedisDsn = "redis://redis:6379/1"
    broker_url: AmqpDsn = "amqp://guest@rabbit:5672//"
    # List of modules to import when the Celery worker starts.
    # imports = ('samurai.samurai_worker',)
    # default task routes
    # task_routes = {"samurai.samurai_worker.samurai.test_celery": "test-queue"}

    task_track_started = True
    class Config:
        env_prefix = "samurai_"
        env_file = ".env"


class ProductionSettings(Settings):
    pass


class TestingSettings(Settings):
    pass


class DevelopmentSettings(Settings):
    pass
