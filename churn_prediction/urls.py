from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('predict/', views.prediction_form, name='prediction_form'),
    path('predict/results/', views.predict_churn, name='predict_churn'),
]