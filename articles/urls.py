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
    # create comment
    path('<int:article_pk>/comments/', views.create_comment, name='create_comment'),
    # delete comment
    # path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
