from django.urls import path
from .views import PostListView,PostDetailtView,PostCreateView,PostUpdateView,PostDeletetView
from . import views # should be inside app folder

urlpatterns = [#included the views and
    path('', PostListView.as_view(), name='Blog-Home'),
    path('posts/<int:pk>/', PostDetailtView.as_view(), name='posts-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='posts-update'),
    path('posts/new/', PostCreateView.as_view(), name='posts-create'),
    path('posts/<int:pk>/delete/', PostDeletetView.as_view(), name='posts-delete'),

    path('about/', views.about, name='Blog-about'),
    
]


