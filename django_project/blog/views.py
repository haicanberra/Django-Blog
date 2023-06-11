from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# New
from django.http import HttpResponse

from .models import Post

# Create your views here.
# Function handles traffic from homepage,
# take in request argument, return what user wants to
# see when sent to this route.

# Dummy data
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Does',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 30, 2018'
#     }
# ]

# def home(request):
# #     return HttpResponse('<h1>blog home</h1>')
#     context = {
#         # 'posts': posts
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-title']
    paginate_by = 5;
    # <app>/<model>_<viewtype>.html

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/' # To home

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # success_url = '/' # To home

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self,):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self,):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5;

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)