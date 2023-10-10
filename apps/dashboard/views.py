from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import UserAccount

from django.views.generic import TemplateView, View
from django.contrib import messages

from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from apps.web.models import Post, Category
from .forms import PostForm

# Create your views here.


def signin(request):
    if request.method == 'GET':
        return render(request, 'pages/signin.html')
    elif request.method == 'POST':
        user = authenticate(
            request, username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'pages/signin.html', {"error": "Username or password is incorrect."})

        login(request, user)
        return redirect('dashboard')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir al inicio de sesión


@login_required
def home(request):
    return render(request, 'dashboard/pages/home.html')
   

"""
@method_decorator(login_required, name='dispatch')
class AddPost(SuccessMessageMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = "dashboard/pages/create.html"
    success_message = "Added Succesfully"

    def get_success_url(self):
        return reverse('create')

"""

@login_required
def add_post(request):
      if request.method == "GET":
           return render(request, 'dashboard/pages/create.html', {'form' : PostForm} )
      elif request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            user = request.user
            try:
                if form.is_valid():
                    new_post = form.save(commit=False)
                    new_post.author = user
                    new_post.published = timezone.now()
                    new_post.save()
                    return redirect ('create')
            except ValueError:
                return render(request, 'dashboard/pages/create.html', {"form": PostForm, "error": "Error creating post."})

    
    
    
@method_decorator(login_required, name='dispatch')  
class PostListView(View):

    def get(self, request, category_name, *args, **kwargs):
        
        category = get_object_or_404(Category, slug=category_name)

        posts = Post.objects.all().filter(category=category)

        return render(request, 'dashboard/pages/posts_list.html', {'posts' : posts })
    
    
    
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'dashboard/pages/post_detail.html', {'post': post, 'form': form})
    elif request.method == 'POST':
        try:
            form = PostForm(request.POST, request.FILES ,instance=post)
            form.save()
            url = reverse('post_detail', args=[post_id])
            return redirect (url)
            
        except ValueError:
            return render(request, 'dashboard/pages/post_detail.html', {'post': post, 'form': form, 'error': 'Error updating post.'})
        
        
@login_required     
def post_delete(request, post_id):
     
    if request.method == 'POST':
         post = get_object_or_404(Post, pk=post_id)
         category = post.category.slug
        
         post.delete()
         
         url = reverse('dash_posts', args=[category])
         return redirect (url)
         
    else:
        return redirect ('dashboard')
    
@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

        
            
    