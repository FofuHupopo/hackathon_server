from django.urls import path

from . import views


urlpatterns = [
    path("", views.RequestView.as_view(), name="request__request"),
    path("create/", views.CreateRequestView.as_view(), name="request__create"),
]
