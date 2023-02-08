from django.urls import (
    path,
)

from . import views

urlpatterns = [
    path('<int:signal>/',view=views.signalPLC,name='ctrl')
]