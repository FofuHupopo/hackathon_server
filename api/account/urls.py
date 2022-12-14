from django.urls import path

from . import views


urlpatterns = [
    path('representative/', views.GetRepresentativeView.as_view(), name="representative__representative"),

    path('representative/passport/', views.PassportView.as_view(), name="representative__passport"),

    path('representative/address/', views.RepresentativeAddressView.as_view(), name="representative__address"),
    path('representative/child/', views.ChildView.as_view(), name="representative__child"),
    path('representative/child/<int:pk>/', views.DetailChildView.as_view(), name="representative__child"),
]
