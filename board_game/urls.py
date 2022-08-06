from django.urls import path
from . import views

urlpatterns = [
    path('', views.Game.as_view()),
    path('user/', views.EditBoard.as_view())
]
