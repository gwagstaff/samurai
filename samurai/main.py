from samurai import samurai_api

app = samurai_api.create_app()
celery = app.worker
