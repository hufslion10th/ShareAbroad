from django.shortcuts import render

# Create your views here. 
def information(request):  # 기존에 이것만 있었음
    return render(request, 'information/information.html')

'''from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "information/index.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "information/post_detail.html"
    context_object = "post"
    pk_url_kwarg = "post_id"

class PostCreateView(CreateView):
    model = Post
    template_name = "information/post_form.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('index')
        #return reverse('post-detail', kwargs={'post-id': self.object.id})

class PostUpdateView(UpdateView):
    model = Post
    template_name = "information/post_form.html"
    form_class = PostForm
    pk_url_kwarg = "post_id"

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post-id': self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "information/post_confirm_delete.html"
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('index')'''