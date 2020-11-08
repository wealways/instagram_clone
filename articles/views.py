from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET

from django.http import JsonResponse
# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')
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
            form = ArticleForm(request.POST,request.FILES,instance=article)
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


# article-delete
@require_POST
def delete(request,article_pk):
    # 유저 로그인되어있는 지 확인
    # 삭제할 article 가져오기
    # article 쓴 사람과 로그인한 사람이 같은 지 확인
    if request.user.is_authenticated:
        article = get_object_or_404(Article,pk=article_pk)
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail',article.pk)


# like
def like(request,article_pk):
    # 좋아요할 게시글 가져오기
    # 좋아요 이미 눌렀는 지 아닌 지 확인해서 데이터 보내기
    if request.user.is_authenticated:
        article = get_object_or_404(Article,pk=article_pk)
        user = request.user
        if article.like_user.filter(pk=user.pk).exists():
            article.like_user.remove(user)
            is_like=False
        else:
            article.like_user.add(user)
            is_like=True
        data={
            'is_like':is_like,
            'like_count':article.like_user.count(),
        }
        return JsonResponse(data)
    return redirect('accounts:login')