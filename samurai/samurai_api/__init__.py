from fastapi import FastAPI

from samurai import samurai_worker

def create_app() -> FastAPI:
    app = FastAPI()

    app.worker = samurai_worker.create_worker()

    from .task_handler import task_router
    app.include_router(task_router)

    @app.get("/")
    async def root():
        return {"message": "Great Success!"}

    return app
