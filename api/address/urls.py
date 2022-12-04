from django.urls import path

from . import views


urlpatterns = [
    path('', views.AddressView.as_view(), name="address__address"),
    path('search/', views.AddressSearchView.as_view(), name="address__search"),
    path('get/', views.AddressGetView.as_view(), name="address__get"),
    
    path('countries/', views.CountryAutoCompleteView.as_view(), name="address__get"),
]
