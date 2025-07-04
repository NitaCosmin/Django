from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main.views import home


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/<int:user_id>/', home, name='user_profile'),
    path('contact/', views.contact, name='contact'),
    path('profil/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('profiles/', views.profiles_list, name='profiles_list'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),

 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)