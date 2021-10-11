from django.urls import path
from board import views

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('', views.board_list, name='board_list'),
    # path('free/', views.board_free, name='board_free'),
    # path('review/', views.board_review, name='board_review'),
    # path('impromptu/', views.board_impromptu, name='board_impromptu'),

    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('create/', views.board_create, name='board_create'),
    path('update/<int:pk>/', views.board_update, name='board_update'),
    path('delete/<int:pk>/', views.board_delete, name='board_delete'),

    path('comment/', views.comment_list, name='comment_list'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('comment/update/<int:pk>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),

    # path('search/<str:keyword>', views.board_search, name='board_search'),
]
