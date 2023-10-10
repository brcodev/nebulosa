from django.urls import path
from .views import signin, home, add_post, PostListView, post_detail, post_delete, signout
urlpatterns = [
   path('', home, name='dashboard'),
   path('create/', add_post, name='create'),
   path('posts/<str:category_name>', PostListView.as_view(), name='dash_posts'),
   path('post/<int:post_id>', post_detail, name='post_detail'),
   path('posts/delete/<int:post_id>', post_delete, name='post_delete'),
   path('logout/', signout, name='logout'),
    
]