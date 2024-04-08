from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("resultados/", views.resultados, name="resultados"),
]