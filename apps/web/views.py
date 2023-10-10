from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from apps.category.models import Category
from django.db.models import Q
from .models import Post

# Create your views here.



class HomeView(View):

    def get(self, request, *args, **kwargs):


        news = Post.objects.filter(category=4).order_by('-id')[:1]
        week = Post.objects.filter(week=True)[:1]
      
        categorias = Category.objects.all()
        posts_category = {}

        for categoria in categorias:
          
            posts = Post.objects.filter(~Q(category__name__in=['Noticias', 'Weeks']), category=categoria).order_by('-published')[:2]
            posts_category[categoria.name] = posts
            
            
        context = {'posts_category': posts_category, 'news' : news, 'week' : week}

        
        return render(request, 'pages/index.html', context)


class ScientistView(View):

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all().filter(category=1).order_by('id')

        return render(request, 'pages/scientist.html', {'posts' : posts })
    
    
    
class ObservatoriestView(View):

    def get(self, request, *args, **kwargs):


        posts = Post.objects.all().filter(category=2).order_by('id')

        
        return render(request, 'pages/observatory.html', {'posts' : posts} )



class TelescopesView(View):

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all().filter(category=3).order_by('id')


        return render(request, 'pages/telescope.html', {'posts' : posts})
    
    
    
class NewsView(View):

    def get(self, request, *args, **kwargs):

        posts = Post.objects.all().filter(category=4).order_by('-id')


        return render(request, 'pages/news.html', {'posts' : posts})
    
    
    
class PostDetail(View):
    
     def get(self, request, slug, *args, **kwargs):
            try:
                detail = Post.objects.get(slug=slug)
                return render(request, 'pages/postDetail.html', {'detail': detail})
            except Post.DoesNotExist:
                return HttpResponse('Pagina no encontrada', status=404)
            
            
def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)
                
         
