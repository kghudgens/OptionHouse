from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Post, Comment

class IndexListView(ListView):
    # Associated the list view with the post view
    model = Post
    # Specified the html to display the list on 
    template_name = 'optionhouseapp/index.html'    
    # Limits the list to show the three most recent posts 
    queryset = Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
class PostDetailView(DetailView):
    model = Post
    template_name= 'optionhouseapp/post-detail.html'
    
class PostListView(ListView):
    model = Post
    template_name = 'optionhouseapp/post-list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'title', 'content', 'image']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('index')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
          
def about(request):
    return render(request, 'optionhouseapp/about.html')