
from django.urls import path
from sheet_app import views

urlpatterns = [
    path('send_email', views.SendEmailToAll.as_view(), name='send_email'),
]