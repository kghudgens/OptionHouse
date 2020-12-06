from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'optionhouseapp/index.html')

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


    
def about(request):
    return render(request, 'optionhouseapp/about.html')