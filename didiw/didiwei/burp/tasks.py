from celery import shared_task


@shared_task
def burp_port(port: str, file: str) -> bool:
    return False
