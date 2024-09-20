from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm, PostForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.http import HttpResponse

import logging


logger = logging.getLogger(__name__)

def test_view(request):
    return HttpResponse("Test view is working!")

def post_list(request):
    print("Entering post_list view")
    posts = Post.objects.all().order_by('-created_at')
    print(f"Number of posts: {posts.count()}")
    for post in posts:
        print(f"Post: {post.title}")
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def serve_image(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if post.image:
            logger.info(f"Serving image for post {post_id}")
            return HttpResponse(post.image, content_type='image/jpeg')
        else:
            logger.warning(f"No image found for post {post_id}")
    except Post.DoesNotExist:
        logger.error(f"Post {post_id} does not exist")
    return HttpResponse(status=404)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            # If the form is not valid, add form errors to messages
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
            # Re-render the page with the form and error messages
            return render(request, 'blog/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'blog/login.html')

@require_POST
@csrf_protect
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('post_list')  # or any other page you want to redirect to after logout

def send_email(name, email, message):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            msg = MIMEMultipart()
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = settings.ADMIN_EMAIL
            msg['Subject'] = f"New contact form submission from {name}"

            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            msg.attach(MIMEText(body, 'plain'))

            smtp.send_message(msg)
            logging.info(f"Email sent successfully to {settings.ADMIN_EMAIL}")

        return True
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
        return False


def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if send_email(name, email, message):
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')

        return redirect('about')

    context = {
        'title': 'About Us',
    }
    return render(request, 'blog/about.html', context)





