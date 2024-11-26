from django.urls import path
from . import views

app_name = 'acc_report'

urlpatterns = [
    path('', views.upload_files, name='upload_files'),
]