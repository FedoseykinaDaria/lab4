from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name = 'HomePage'),
    path('form/', views.HealthForm, name = 'HealthForm'),
    path('file/', views.UploadedFileForm, name = "UploadedFileForm"),
    path('showJSON/<str:name>/', views.JSONInfo, name = 'JSONInfo'),
    path('showDB/<int:note_id>/', views.DBInfo, name = 'DBInfo'),
    path('search/', views.DBSearch, name = 'DBSearch')
]