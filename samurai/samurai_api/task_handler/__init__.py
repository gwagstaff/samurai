from fastapi import APIRouter

task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

from . import tasks # noqa
