from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForms

def get_base_context():
    posts = Post.objects.filter(published_date__isnull=False)
    return {
        'total_posts': posts.count(),
        'liked_posts_count': 2,  # Valores de ejemplo
        'bookmarked_posts_count': 5,  # Valores de ejemplo
        'popular_posts_count': 3,  # Valores de ejemplo
        'programming_posts_count': 8,  # Valores de ejemplo
        'design_posts_count': 3,  # Valores de ejemplo
        'tech_posts_count': 6,  # Valores de ejemplo
        'tutorial_posts_count': 4,  # Valores de ejemplo
        'popular_posts': posts.order_by('-created_date')[:3],  # 3 posts más recientes
        'popular_tags': [],  # Lista vacía
        'total_views': posts.count() * 25,  # Aproximación de vistas
        'total_comments': posts.count() * 3,  # Aproximación de comentarios
        'total_likes': posts.count() * 7,  # Aproximación de likes
    }

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    context = get_base_context()
    context['posts'] = posts
    
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = get_base_context()
    context['post'] = post
    
    return render(request, 'blog/details.html', context)

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})