from django.urls import path
from . import views

urlpatterns = [
    ## views.py의 index호출
    path('board/', views.show_board, name='show_board'),
    path('data/form/', views.data_form, name='data_form'),
    path('data/form2/', views.data_form2, name='data_form2'),
    path('data/view/', views.data_form, name='board_result')
]