from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog_app'

urlpatterns =[
    path(r'about/',views.AboutView.as_view(),name= 'about'),
    path(r'', views.BlogPostListView.as_view(),name = 'blogpost_list'),
    path('blogpost/<int:pk>/', views.BlogPostDetailView.as_view(),name = 'blogpost_detail'),
    path('blogpost/create/',views.BlogPostCreateView.as_view(),name ='blogpost_create'),
    path('blogpost/<int:pk>/edit/', views.BlogPostUpdateView.as_view(),name = 'blogpost_edit'),
    path('blogpost/<int:pk>/delete/', views.BlogPostDeleteView.as_view(),name = 'blogpost_delete'),
    path('drafts/', views.DraftListView.as_view(),name = 'blogpost_draft_list'),
    path('blogpost/<int:pk>/comment/', views.add_comment_to_blogpost,name = 'add_comment_to_blogpost'),
    path('blogpost/<int:pk>/publish/', views.blogpost_publish,name = 'blogpost_publish'),
    path('comment/<int:pk>/approve/', views.comment_approve,name = 'comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remover,name = 'comment_remove'),
    
]