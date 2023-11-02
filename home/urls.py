from django.urls import path

from home.views import HomeView, TakeTestView, AnswerView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('test/<str:slug>/', TakeTestView.as_view(), name='take-test'),
    path('answer/', AnswerView.as_view(), name='create-answer')
]