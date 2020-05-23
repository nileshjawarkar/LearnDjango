from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.http import HttpResponse

from blog.forms import PostForm, PostFormReadonly

from .models import Post, Comment

@login_required
def my_posts( request, pk=None ) :
    posts = Post.objects.filter(author=request.user)
    form = None
    if len(posts) > 0 :
        if pk == None :
            pk = posts[0].pk
            return HttpResponseRedirect(reverse("blog:my_post_selected", kwargs={'pk': pk}))
        post_details = Post.objects.get(pk=pk)
        form = PostFormReadonly(instance=post_details)

    context = {
        "posts" : posts, 
        "form" : form,
        "form_pk" : pk,
        "form_type" : "readonly"
    }
    return render( request, "blog/my_post.html", context)

@login_required
def my_posts_new( request ) :

    post_details = None
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse("blog:my_post_selected", kwargs={'pk': post.pk}))

    posts = Post.objects.filter(author=request.user)
    form = PostForm()        
    context = {
        "posts" : posts, 
        "form" : form,
        "form_pk" : None,
        "form_type" : "new"
    }
    return render( request, "blog/my_post.html", context)


@login_required
def my_posts_edit( request, pk ) :

    post_details = None
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")

        post_details = Post.objects.get(pk=pk)
        post_details.title = title
        post_details.text = text
        post_details.save()
        return HttpResponseRedirect(reverse("blog:my_post_selected", kwargs={'pk': pk}))

    posts = Post.objects.filter(author=request.user)
    form = None
    if len(posts) > 0 :
        if pk == None :
            pk = posts[0].pk

    if request.method == "GET" :
        post_details = Post.objects.get(pk=pk) 

    form = PostForm(instance=post_details)
        
    context = {
        "posts" : posts, 
        "form" : form,
        "form_pk" : pk,
        "form_type" : "edit"
    }
    return render( request, "blog/my_post.html", context)

@login_required
def my_posts_delete( request, pk) :

    if request.method == "POST" :
        post_details = Post.objects.get(pk=pk)   
        post_details.delete()
        pk = None
        return HttpResponseRedirect( reverse("blog:my_post") )

    posts = Post.objects.filter(author=request.user)
    form = None
    if len(posts) > 0 :
        if pk == None :
            pk = posts[0].pk
        post_details = Post.objects.get(pk=pk) 
        form = PostForm(instance=post_details)

    context = {
        "posts" : posts, 
        "form" : form,
        "form_pk" : pk,
        "form_type" : "delete"
    }
    return render( request, "blog/my_post.html", context)

# def create_post( request ) :
#     form = None
#     if request.method == "POST" :
#         form = PostForm( request.POST )
#         if form.is_valid() :
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return HttpResponseRedirect( reverse("home") )
#     else :
#         form = PostForm()
#     return render( request, "blog/post_form.html", { "form" : form })

class PostCreateView( CreateView ) :
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView( ListView ) :
    model = Post
    paginate_by = 10