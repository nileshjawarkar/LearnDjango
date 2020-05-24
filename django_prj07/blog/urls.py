from django.urls import path
# from blog.views import my_posts_create_update, my_posts, my_posts_edit, my_posts_delete
from blog.views import list_my_posts, create_or_update_my_posts, delete_my_posts

app_name = "blog"

urlpatterns = [
    path('post', list_my_posts, name='post_list'),  
    path('post/<int:pk>', list_my_posts, name='post_list_selected'),
    path('post/<int:pk>/edit', create_or_update_my_posts, name='post_edit'),
    path('post/<int:pk>/delete', delete_my_posts, name='post_delete'),    
    path('post/create', create_or_update_my_posts, name='post_create'),
]
