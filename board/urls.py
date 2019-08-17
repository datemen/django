from django.urls import path
from . import views

urlpatterns = [
        path('',views.board_index,name='board_index'),
        path('first_topic/<str:first_topic_name>',views.second_topic_page,name='board_second_topic'),
        path('first_topic/<str:first_topic_name>/<str:second_topic_name>',views.third_topic_page,name='board_third_topic'),
        path('first_topic/<str:first_topic_name>/<str:second_topic_name>/<str:third_topic_name>',views.board,name='board'),
        path('search_result/<str:search_word>',views.search_result,name='search_result'),
        path('ranking',views.ranking_page,name='ranking_page'),
        ]