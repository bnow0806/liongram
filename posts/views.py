from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic.list import ListView

from .models import Post  
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_at') #Post 전체 데이터 조회, 역순
    context={
        'post_list' : post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.all()  # Post 전체 데이터 조회
    #post_list = Post.objects.filter(writer = request.user) #Writer filter
    context={
        'post_list' : post_list,
    }
    return render(request, 'posts/post_list.html', context) 

#@login_required
def post_create_view(request):
    if request.method =='GET': #페이지 불러올때
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer = request.user
        )
        return redirect('index')

def post_detail_view(request, id):
    try:
        post=Post.objects.get(id =id)
    except Post.DoesNotExist:
        return redirect('index')
    context={
        'post':post,
    }
    return render(request, 'posts/post_detail.html', context) 

def post_update_view(request, id):
    #post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.method =='GET':
        context = {'post' : post}
        return render(request, 'posts/post_form.html', context)
    elif request.method =='POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')

        if new_image:
            post.image.delete()     #기존 이미지 삭제
            post.image = new_image  #새 이미지 추가

        post.content = content
        post.save()

        return redirect('posts:post-detail', post.id)

def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)

    # if request.user != post.writer:
    #     return Http404('잘못된 접근입니다.')

    if request.method == 'GET':
        context = {'post': post}
        return render(request, 'posts/post_conform_delete.html', context)
    else:
        post.delete()
        return redirect('index')

def url_view(request):
    data = {'ok':True}
    #return HttpResponse('<h1>url_view</h1>')
    return JsonResponse(data)

def url_parameter_view(request, username):
    print(username)
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method : {request.method}')
    print(f'request.GET : {request.GET}')
    print(f'request.POST : {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name ='cbv_view.html'