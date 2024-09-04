from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Use custom login view
    path('logout/', views.logout_view, name='logout'),  # Updated to use custom logout view
    path('about/', views.about, name='about'),
    path('test/', views.test_view, name='test_view'),

    # ... other paths ...
]