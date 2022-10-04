from time import sleep
from celery import shared_task


@shared_task(bind=True, acks_late=True)
def test_celery(self, word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        self.update_state(state='PROGRESS',
                          meta={'process_percent': i * 10})
    return f"test task return {word}"
