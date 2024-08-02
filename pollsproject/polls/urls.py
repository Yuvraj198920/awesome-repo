from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("item/", view=views.item, name="item"),
]
