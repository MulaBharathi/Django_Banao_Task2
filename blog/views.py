from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm

@login_required
def create_blog_post(request):
    if not request.user.is_doctor:
        return redirect('home')  # or permission denied page

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def doctor_blog_posts(request):
    if not request.user.is_doctor:
        return redirect('home')

    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_blog_posts.html', {'posts': posts})

def patient_blog_list(request, category_id=None):
    categories = Category.objects.all()
    posts = BlogPost.objects.filter(draft=False)
    if category_id:
        posts = posts.filter(category_id=category_id)
    return render(request, 'blog/patient_blog_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    })

