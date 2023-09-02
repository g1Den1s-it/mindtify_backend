from django.urls import path

from user.views import RegistrationView

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='registration')
]
