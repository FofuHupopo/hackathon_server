from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='auth__registration'),
    path('logout/', views.UserLogoutView.as_view(), name='auth__logout'),

    path('token/', views.CookieTokenObtainPairView.as_view(), name='auth__token_obtain_pair'),
    path('token/refresh/', views.CookieTokenRefreshView.as_view(), name='auth__token_refresh'),
    
    path('code/send/', views.SendCodeView.as_view(), name='auth__send_code'),
    path('code/confirm/', views.ConfirmCodeView.as_view(), name='auth__confirm_code'),
]
