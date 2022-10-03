from fastapi import BackgroundTasks

from samurai import samurai_worker
from samurai.samurai_utils import utils

from . import task_router

worker = samurai_worker.create_worker()


@task_router.get("/{word}")
async def root(word: str, background_task: BackgroundTasks):
    task_name = "samurai.samurai_worker.samurai.test_celery"

    task = worker.send_task(task_name, args=[word])
    print(task)
    background_task.add_task(utils.background_on_message, task)

    return {"message": "Word received"}




