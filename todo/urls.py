from django.urls import path
from .views import index, async_view

urlpatterns = [
    path('', index, name="home"),
    path('async', async_view, name="async"),
]
