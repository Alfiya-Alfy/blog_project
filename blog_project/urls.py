from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blogapp import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),  # App routes
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout/Password
    path('register/', blog_views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
