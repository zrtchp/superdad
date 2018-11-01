from django.shortcuts import render, get_object_or_404
from .models import blogarticles
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def blog_title(request):
    blogs=blogarticles.objects.all()
    return render(request, 'blog/titles.html', {"blogs":blogs})

def blog_article(request,article_id):
    #article = blogarticles.objects.get(id=article_id)
    article = get_object_or_404(blogarticles,id=article_id)
    pub=article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub })

def home(request):
    HttpResponseRedirect(reverse_lazy('blog:blog_title'))