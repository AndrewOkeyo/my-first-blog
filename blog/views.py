from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.db import connection
import pymysql
import pymysql.cursors
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_exempt


def index(response):
    conn = pymysql.connect('127.0.0.1', 'root', '', 'books', charset='utf8mb4', 
                           cursorclass=pymysql.cursors.DictCursor)
    
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM blog_post")
        rows = cur.fetchall()
        temp =  get_template("blog/index.html")
        return HttpResponse(temp.render({'blogs': rows}))

def post_detail(request, pk):
    
    conn = pymysql.connect('127.0.0.1', 'root', '', 'books', charset='utf8mb4', 
                            cursorclass = pymysql.cursors.DictCursor)

    with conn:
        #blog = get_object_or_404(Post, pk=pk)
        cur = conn.cursor()
        cur.execute("SELECT * FROM blog_post WHERE id=%s", pk)
        blog = cur.fetchone()
        temp = get_template('blog/post_detail.html')
        return HttpResponse(temp.render({'blog': blog}))



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author  = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostForm()
    temp = get_template('blog/post_new.html')
    return HttpResponse(temp.render({'form': form}))



def edit_post(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author  = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostForm(instance=post)
    temp = get_template('blog/post_new.html')
    return HttpResponse(temp.render({'form': form}))

