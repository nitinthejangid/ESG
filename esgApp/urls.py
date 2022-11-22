from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('getAnalyzedData/', views.getAnalyzedData)
]