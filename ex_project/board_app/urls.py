from django.urls import path
from . import views

urlpatterns = [
    ## views.py의 index호출
    path('board/', views.show_board, name='show_board'),
    path('data/form/', views.data_form, name='data_form'),
    path('data/form2/', views.data_form2, name='data_form2'),
    path('data/view/', views.data_form, name='board_result')
]
# urls에 path를 동록하여 사용할 페이지의 링크를 지정한다
# html파일 하나당 하나씩 쓰는듯 보통
