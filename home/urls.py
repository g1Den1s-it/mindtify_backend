from django.urls import path

from home.views import HomeView, TakeTestView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('test/<str:slug>/', TakeTestView.as_view(), name='take-test')
]