from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@require_http_methods(['GET','POST'])
@login_required
def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context={
        'form':form,
    }
    return render(request,'articles/form.html',context)


def detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)


@require_http_methods(['GET','POST'])
@login_required
def update(request,article_pk):
    # 업데이터를 하려면, 원래 데이터 가져오기
    article = get_object_or_404(Article,pk=article_pk)
    # 시도하는 유저와 글 쓴 유저가 같나요?
    if request.user == article.user:
        # post방식인가요?
        if request.method == 'POST':
            form = ArticleForm(request.POST,instance=article)
            # 유효성 검사할까요
            if form.is_valid():
                form.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail',article.pk)
    context={
        'form':form,
    }
    return render(request,'articles/form.html',context)