from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),

    path('post/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('post/new/', views.post_create_view, name='post-create'),
    path('post/<int:pk>/edit/', views.post_edit_view, name='post-edit'),
    path('post/<int:pk>/delete/', views.post_delete_view, name='post-delete'),

    path('comment/<int:pk>/edit/', views.comment_edit_view, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='comment-delete'),

    path('profile/', views.profile_view, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
]
