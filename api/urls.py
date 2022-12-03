from django.urls import path, include


urlpatterns = [
    path('auth/', include('api.authentication.urls')),
    path('account/', include('api.account.urls')),
    path('address/', include('api.address.urls')),
    # path('camp/', include('api.camp.urls')),
]
