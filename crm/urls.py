from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.CampListView.as_view(), name="crm")
]
