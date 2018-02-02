from django.views.generic import ListView
from django.views.generic import DetailView

from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'bbin'