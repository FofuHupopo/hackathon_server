from django.urls import path

from . import views


urlpatterns = [
    path(
        'filter/', views.CampEventView.as_view(),
        name="camp__camp_event_filter")
]
