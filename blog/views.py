from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from .forms import ArticleForm
# Create your views here.



def index(request):
    yangiliklar = Article.objects.all().order_by('-id')
    kategoriyalar = Category.objects.all()
    
    context = {
        'yangiliklar': yangiliklar,
        'kategoriyalar': kategoriyalar
    }
    
    return render(request, 'index.html', context)


def detail(request, id):
    # yangilik = Article.objects.get(id=id)
    yangilik = get_object_or_404(Article, id=id)
    yangilik.views += 1
    yangilik.save()
    
    other_news = Article.objects.all().exclude(id=id).order_by('-id')[:3]
    context = {
        "news": yangilik,
        "other_news":other_news
    }
    
    return render(request, 'detail.html', context)





def category_list(request, id):
    ctg = get_object_or_404(Category, id=id)
    news = Article.objects.filter(category__id = id)
    kategoriyalar = Category.objects.all()
    
    context = {
        'ctg': ctg,
        'news': news,
        'kategoriyalar': kategoriyalar
    }
    
    return render(request, 'category_news.html', context)



def create_article(request):
    form = ArticleForm()
    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        return redirect('home')
        
    
def update_article(request, id):
    if request.method == 'GET':
            
        news = get_object_or_404(Article, id=id)
        form = ArticleForm(instance=news)
        context = {
            'form': form
        }
        return render(request, 'update.html', context)
    
    elif request.method == 'POST':

        yangilik = Article.objects.get(id=id)
        form = ArticleForm(request.POST, request.FILES, instance=yangilik)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'update.html', context)
        
        
def delete_article(request, id):
    yangilik = Article.objects.get(id=id)
    context = {
        'news':yangilik
    }
    return render(request, 'delete.html', context)

def delete(request, id):
    yangilik = Article.objects.get(id=id)
    yangilik.delete()
    return redirect('home')