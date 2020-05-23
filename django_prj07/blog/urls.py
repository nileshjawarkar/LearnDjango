from django.urls import path
from blog.views import my_posts_new, my_posts, my_posts_edit, my_posts_delete

app_name = "blog"

urlpatterns = [
    path('post', my_posts, name='my_post'),  
    path('post/<int:pk>', my_posts, name='my_post_selected'),
    path('post/<int:pk>/edit', my_posts_edit, name='my_post_edit'),
    path('post/<int:pk>/delete', my_posts_delete, name='my_post_delete'),    
    path('post/create', my_posts_new, name='my_post_create'),
]
