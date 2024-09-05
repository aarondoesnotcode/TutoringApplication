from django.urls import path
from . import views

# configuring URL
urlpatterns = [
    path("", views.test),
    path('test/', views.test2)
]