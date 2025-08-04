from django.contrib import admin
from django.urls import path
from notes import views
from django.contrib.auth import views as auth_views
from notes.views import create_note_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.add_note, name='add_note'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('api/create-note/', create_note_api, name='create_note_api'),
  
]
