from django.urls import path
from . import views

urlpatterns = [
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
    path('', views.buscar_post, name='inicio'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('autores/', views.lista_autores, name='lista_autores'),
]
