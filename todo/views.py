from django.http import HttpResponse
import asyncio
import time


async def index(request):
    await asyncio.sleep(0.5)
    return HttpResponse('Hello, async world!')


def async_view(request):
    start_time = time.time()
    total = (time.time() - start_time)
    print(f"Total: {total}")
    return HttpResponse('async')
