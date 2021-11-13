from django.shortcuts import render, redirect
from .models import Blog
from .forms import AddBlogs
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def blog(request):

    if request.method == 'POST':
        form = AddBlogs(request.POST)
        if form.is_valid():
            blog = Blog()
            blog.title = request.POST.get('title')
            blog.content = request.POST.get('content')
            blog.image = request.POST.get('image')
            blog.save()
            return redirect('/blog')

        elif request.method == 'POST':
            id = request.POST.get('id')
            Blog.objects.filter(id=id).delete()
            return redirect('/blog')

    blogs = Blog.objects.all()
    context = {'blogs': blogs, 'addBlogs': AddBlogs()}

    return render(request, 'Blog/blog.html', context)
