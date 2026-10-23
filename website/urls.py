from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cursos/", views.course_list, name="course_list"),
    path("cursos/<slug:slug>/", views.course_detail, name="course_detail"),
    path("noticias/", views.news_list, name="news_list"),
    path("noticias/<slug:slug>/", views.news_detail, name="news_detail"),
    path("contactos/enviar/", views.contact, name="contact"),
]
