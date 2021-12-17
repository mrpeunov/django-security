from django.shortcuts import render
from django.http import JsonResponse
from case3.models import Post


def create_post(request):
    text = request.POST.get('text')
    Post.objects.create(text=text)
    return JsonResponse({"text": text}, status=201)


def get_post(request):
    posts = Post.objects.all()
    return render(request, 'case3.html', locals())

