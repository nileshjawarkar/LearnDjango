from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.http import HttpResponse

from blog.forms import PostForm, PostFormReadonly

from .models import Post, Comment


def render_post( request, all_post, form, form_type, form_pk=None ) :
    context = {
        "posts" : all_post, 
        "form" : form,
        "form_pk" : form_pk,
        "form_type" : form_type
    }
    return render( request, "blog/my_post.html", context)

@login_required
def list_my_posts( request, pk=None ) :
    posts = Post.objects.filter(author=request.user)
    form = None
    if len(posts) > 0 :

        # Redirect if pk is None
        if pk == None :
            pk = posts[0].pk
            return HttpResponseRedirect(reverse("blog:post_list_selected", kwargs={'pk': pk}))
        post_details = Post.objects.get(pk=pk)
        form = PostFormReadonly(instance=post_details)

    return render_post( request, posts, form, "readonly",  pk )


@login_required
def create_or_update_my_posts( request, pk = None ) :

    post_details = None
    form_type = "new"
    if pk is not None :
        form_type = "edit"

    form = None
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            # create
            if pk is None :
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                pk = post.pk                
            # update
            else :            
                title = form.cleaned_data.get("title")
                text = form.cleaned_data.get("text")

                # update the data
                post_details = Post.objects.get(pk=pk)
                post_details.title = title
                post_details.text = text
                post_details.save()
            # redirect to show current updated or created post
            return HttpResponseRedirect(reverse("blog:post_list_selected", kwargs={'pk': pk }))
    else :
        # Create
        if pk is None :
            form = PostForm()
        # update : Show edit from for post related to pk
        else :
            post_details = Post.objects.get(pk=pk)
            form = PostForm(instance=post_details)       

    posts = Post.objects.filter(author=request.user)
    return render_post( request, posts, form, form_type,  pk )    


# @login_required
# def my_posts_edit( request, pk ) :

#     post_details = None
#     if request.method == "POST" :
#         form = PostForm(request.POST)
#         if form.is_valid() :
#             title = form.cleaned_data.get("title")
#             text = form.cleaned_data.get("text")

#         post_details = Post.objects.get(pk=pk)
#         post_details.title = title
#         post_details.text = text
#         post_details.save()
#         return HttpResponseRedirect(reverse("blog:my_post_selected", kwargs={'pk': pk}))

#     posts = Post.objects.filter(author=request.user)
#     if request.method == "GET" :
#         post_details = Post.objects.get(pk=pk) 

#     form = PostForm(instance=post_details)
#     return render_post( request, posts, form,  "edit",  pk )  

@login_required
def delete_my_posts( request, pk) :

    if request.method == "POST" :
        post_details = Post.objects.get(pk=pk)   
        post_details.delete()
        pk = None
        return HttpResponseRedirect( reverse("blog:post_list") )

    posts = Post.objects.filter(author=request.user)
    form = None
    if len(posts) > 0 :
        if pk == None :
            pk = posts[0].pk
        post_details = Post.objects.get(pk=pk) 
        form = PostForm(instance=post_details)

    return render_post( request, posts, form,  "delete",  pk ) 


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

# class PostCreateView( CreateView ) :
#     model = Post
#     form_class = PostForm
#     success_url = reverse_lazy("home")

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostListView( ListView ) :
#     model = Post
#     paginate_by = 10