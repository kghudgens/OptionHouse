from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'optionhouseapp/index.html')

class IndexListView(ListView):
    model = Post
    template_name = 'optionhouseapp/index.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
    