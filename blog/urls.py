from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about-me/', views.about_me, name='about-me'),
    path('about-website/', views.about_website, name='about-website'),
    path('projects/', views.projects, name='projects'),
    path('web-programming/', views.web_programming, name='web-programming'),
    path('contact/', views.contact, name='contact'),
    path('javascript/', views.javascript, name='javascript'),
    path('blog/', views.blog_posts, name='blog_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),


    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('apagar/<int:post_id>/', views.apagar_post, name='apagar_post'),
    path('adicionar_autor/', views.adicionar_autor, name='adicionar_autor'),
]