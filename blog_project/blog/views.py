from django.views.generic import ListView,DetailView,CreateView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'bbin'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body',]
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name='post_delete.html'
    success_url = reverse_lazy('home')