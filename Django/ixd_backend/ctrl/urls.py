from django.urls import (
    path,
)

from . import views

urlpatterns = [
    path('<int:ean>/',view=views.signalPLC,name='ctrl')
]