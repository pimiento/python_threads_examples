# Create your tasks here
from typing import Union, List, Tuple
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def countdown(n=int(5e8)):
    for _ in n:
        n -= 1
    return n

@shared_task
def send_notification(subj: str, text: str, send_from: str, send_to: Union[List[str], Tuple[str]]):
    send_mail(subj, text, send_from, send_to, fail_silently=False)
    return "SENT"
