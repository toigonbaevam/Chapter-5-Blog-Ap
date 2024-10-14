from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    
class BlogDetailView(DetailView): 
    model = Post
    template_name = "post_detail.html"
    
    
    
    
    

from django.shortcuts import render
from django.views import View

class PostCreateView(View):
    def get(self, request):
        return render(request, 'post_new.html') 

from .views import PostCreateView

