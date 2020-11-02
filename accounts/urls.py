from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    # create
    path('signup/',views.signup,name='signup'),
    # create session
    path('login/', views.login, name='login'),
    # # delete session
    path('logout/', views.logout, name='logout'),
    # profile
    # follow
    path('update/',views.update,name='update'),
    path('<username>/',views.profile,name='profile'),
]
