from django.contrib import admin
from django.urls import path
from article import views

app_name= "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createarticle/', views.createArticle, name="createarticle"),
    path('article/<int:id>',views.showDetail,name="showdetail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('', views.articles, name="article"),
    path('comment/<int:id>',views.addComment,name="comment"),
]
