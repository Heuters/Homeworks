rom django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from .forms import CreatePostForm
from blog.models import Post
from blog.constants import PAGINTION_LIMIT


def post_list_view(request):
    print(request.user)
    if request.method == 'GET':
        post_value = Post
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            post_value = post_value.filter(title__contains=search) | post_value.filter(description_contains=search)

        max_page = post_value.__len__() / PAGINTION_LIMIT
        if round(max_page) == round(max_page) + 1:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        post_value = post_value[PAGINTION_LIMIT * (page-1):PAGINTION_LIMIT*page]

        context_data = {
            'post_key': post_value,
            'user': request.user,
            'pages': range(1, max_page+1)
        }

        return render(request, 'post/post.html', context=context_data)



def post_create_view(request):
    if request.method == 'GET':
        contex_data = {
            'form': CreatePostForm
        }

        return render(request, 'post/create.html', context=contex_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreatePostForm(data, files)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            Post.objects.create(
                image=cleaned_data.get('image'),
                title=cleaned_data.get('title'),
                description=cleaned_data.get('description'),
                cost=cleaned_data.get('cost'),
                director=cleaned_data.get('director'),
                number_of_page=cleaned_data.get('number_of_page'),)
            return redirect('/post/')

    return render(request, '/post/create.html', context={'form': form})

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello! Its my project</h1>')


def now_data_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>17.10.23</h1>')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Goodbye user!</h1>')


def post_detail_view(request, id):
    if request.method == 'GET':
        post = get_object_or_404(models.Post, id=id)

        context_data = {
            'post': post
        }
        return render(request, 'post/post_detail.html', context=context_data)