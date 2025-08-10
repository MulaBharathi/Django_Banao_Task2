from django.urls import path
from . import views

urlpatterns = [
    path('doctor/blog/create/', views.create_blog_post, name='create_blog_post'),
    path('doctor/blog/posts/', views.doctor_blog_posts, name='doctor_blog_posts'),
    path('blogs/', views.patient_blog_list, name='patient_blog_list'),
    path('blogs/category/<int:category_id>/', views.patient_blog_list, name='patient_blog_list_by_category'),
]i

