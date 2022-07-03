from django.shortcuts import render

# Views take from model and pass to template Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html',{})
