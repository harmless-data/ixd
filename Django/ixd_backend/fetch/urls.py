from django.urls import (
    # re_path,
    path,
)

from . import views

urlpatterns = [
    path('',views.fetchIndex, name="fetchIndex"),
    path('EAN/<int:ean>/',views.fetchEAN, name="fetchEAN"),
    # re_path(r'EAN/(?P<ean>\d+)/$',views.fetchEAN, name="fetchEAN"),
    path('LIST/',views.fetchList, name="fetchList"),
    path('ADD/<int:ean>/',views.addToStatic,name='addStatic'),
]