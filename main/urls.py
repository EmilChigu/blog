from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('article/<str:pk>', views.article, name='article'),
    path('create-article/', views.createArticle, name='create-article'),
    path('update-article/<str:pk>', views.updateArticle, name='update-article'),
    path('delete-article/<str:pk>', views.deleteArticle, name='delete-article'),
    path('delete-comment/<str:pk>', views.deleteComment, name='delete-comment'),
]
