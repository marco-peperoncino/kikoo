from django.views.generic import ListView
from .models import Post
from django.shortcuts import render


class PostListView(ListView):
    model = Post
    template_name = "tweet/imdex.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
