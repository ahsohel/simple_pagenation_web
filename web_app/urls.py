from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page_2', views.page_2, name='page_2'),
]