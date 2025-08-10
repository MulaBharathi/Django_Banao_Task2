from django.urls import path
from . import views

urlpatterns = [
    # Root URL (http://127.0.0.1:8000/) shows all published blogs to patients
    path('', views.patient_blog_list, name='patient_blog_list_root'),

    # Doctor URLs
    path('doctor/blog/create/', views.create_blog_post, name='create_blog_post'),
    path('doctor/blog/posts/', views.doctor_blog_posts, name='doctor_blog_posts'),

    # Patient URLs to view blogs by category and all blogs
    path('blogs/', views.patient_blog_list, name='patient_blog_list'),
    path('blogs/category/<int:category_id>/', views.patient_blog_list, name='patient_blog_list_by_category'),
]

