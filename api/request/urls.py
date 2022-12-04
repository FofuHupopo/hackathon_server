from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreateRequestView.as_view(), name="request__create"),
]
