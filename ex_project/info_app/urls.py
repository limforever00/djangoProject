from django.urls import path
from . import views

urlpatterns = [
    ## views.py의 index호출
    path('', views.index, name='index'),
    path('img/', views.show_info, name='show_info'),
]