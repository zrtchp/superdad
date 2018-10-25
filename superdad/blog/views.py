from django.shortcuts import render
from .models import blogarticles

def blog_title(request):
    blogs=blogarticles.objects.all()
    return render(request, 'blog/titles.html', {"blogs":blogs})
# Create your views here.
def blog_article(request,article_id):
    article = blogarticles.objects.get(id=article_id)
    pub=article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub })