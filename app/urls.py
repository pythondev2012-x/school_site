from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('blog-detail/<int:id>',views.blog_detail,name='detail'),
    path('category/<int:id>/', views.blog_category_list, name='category_blogs'),
    path('lesson/<int:id>/', views.lesson_detail, name='detail_lesson'),
    path('teacher/<int:id>/', views.teacher_detail, name='detail_teacher'),
]
