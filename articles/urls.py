from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:article_pk>/',views.detail,name='detail'),
    #update
    path('<int:article_pk>/update/',views.update,name='update'),
    #delete
    path('<int:article_pk>/delete/',views.delete,name='delete'),
    # like
    path('<int:article_pk>/like/',views.like,name='like'),
]
