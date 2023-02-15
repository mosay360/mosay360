from django.shortcuts import render
from django.contrib.postgres.search import  SearchVector
from email import message
from multiprocessing import context
from re import search
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from blog.models import Post, Comment
from typing import List
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.postgres.search import SearchVector
from .forms import CommentForm, PostForm, EditForm , EmailPostForm 
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm ,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

# Create your views here.


def BlogIndex(request, tag_slug=None):
    object_list= Post.published.all()
    ordering=['-publish']
    tag= None
    if tag_slug:
        tag= get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in = [tag])
    paginator= Paginator(object_list, 3)
    page= request.GET.get('page')
    try:

        posts = paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts =paginator.page(paginator.num_pages)

       

    return render(request, 'blog/blogIndex.html',
    {'page':page, 'posts':posts, 
    'tag':tag
    }
    )
    
    
def Blog( request):
    
    return render(request, 'blogIndex.html')

    
    
 #Detail views
def PostDetail(request, year, month, day, post):
    post=get_object_or_404(
    Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day
    )


    #List of active comments for this post

    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST)
    if request.method == 'POST':
        #posted comment
       
      if comment_form.is_valid():

        new_comment = comment_form.save(commit=False)
        new_comment.post= post
        new_comment.save()
    else: 
        comment_form = CommentForm()


        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request, 'blog/postDetail.html',{'post':post, 'new_comment':new_comment, 'comments':comments, 'comment_form':comment_form,
    })

def post_share(request, post_id):

    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False    


    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
        post_url = request.build_absolute_uri(
        post.get_absolute_url())
        subject = f"{cd['name']} recommends you read " 
        f"{post.title}"
        message = f"Read {post.title} at {post_url}" 
        f"{cd['name']}'s comments: {cd['comments']}"
        send_mail(subject, message, 'mosay360@gmail.com', [cd['to']])
        sent = True
    else: 
            form = EmailPostForm()
    return render(request, 'blog/share.html',{'post':post, 'form':form
    ,'sent':sent})




#def blogIndex(request):

   # object_list = Post.published.all()
    #ordering = ['-publish']
   # paginator= Paginator(object_list, 3)
    #page = request.GET.get('page')
    #try:
       # posts= paginator.page(page)
   # except PageNotAnInteger:
       # posts= paginator.page(1)
    #except EmptyPage:
       # posts=paginator.page(paginator.num_pages)

   # return render(request, 'blog/blogIndex.html',{'page':page,'posts':posts})


class BlogView(ListView):
    model = Post
    template_name = 'blog/blogIndex.html'
    ordering = ['-created']



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    #fields ='__all__'


class AddCategoryView(CreateView):
    
    #form_class = PostForm
    template_name = 'blog/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    #fields =['title','title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blogIndex')

def postSearch(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        posts= Post.objects.filter(body__contains=searched )
        

        return render(request, 
        'blog/search.html',{'searched':searched, 'posts':posts})
    else:
         return render(request, 
        'blog/search.html',{})

def Slider(request):
    slide = Slider.object.all()
    context ={
        'slider':Slider
    }  
    return render(request, "blog/slider.html")

