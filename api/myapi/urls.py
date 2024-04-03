from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('teachers/', views.teacher),
    path('students/', views.student),
]
