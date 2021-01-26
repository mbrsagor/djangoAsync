from django.http import HttpResponse
from asgiref.sync import sync_to_async
import asyncio
import time

from .models import Task


def get_task():
    time.sleep(10)
    qs = Task.objects.all()
    print(qs)


async def index(request):
    await asyncio.sleep(0.5)
    return HttpResponse('Hello, async world!')


def async_view(request):
    start_time = time.time()
    get_task()
    total = (time.time() - start_time)
    print(f"Total: {total}")
    return HttpResponse('async')


@sync_to_async
def get_async_task():
    time.sleep(10)
    qs = Task.objects.all()
    print(qs)
    print("Get all task")


async def async_task_view(request):
    pass
