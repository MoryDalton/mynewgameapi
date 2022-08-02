from django.urls import path
from . import views


urlpatterns = [
    path('', views.Myview.as_view()),
    path('user/<id>/', views.MyViewUser.as_view()),
]
