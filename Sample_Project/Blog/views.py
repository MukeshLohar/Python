from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from .models import posts

# Create your views here.


def home(request):  #creating the home route for
    context = {'article': posts.objects.all()}
    return render(request, 'Blog/home.html', context)


class PostListView(ListView):
    model = posts
    template_name = 'Blog/home.html'
    context_object_name = 'article'
    ordering = ['-date_posted']


class PostDetailtView(DetailView):
    model = posts

class PostDeletetView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = posts
    success_url = '/'
    def test_func(self):
        posts = self.get_object()
        if self.request.user == posts.author :
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model = posts
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = posts
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        posts = self.get_object()
        if self.request.user == posts.author :
            return True
        return False


def about(request):
    return render(request, 'Blog/about.html',
                  {'title': 'About'})  #directly passing dict for context
