from django.urls import path
from . import views
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

# Empty path for homepage (from 
# /blog linked in projects urls)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # <app>/<model>_<viewtype>.html
    path('about/', views.about, name='blog-about')
]