from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blogs.views_public import HandleEditorUpload
from home import views_public

urlpatterns = [
    path('', views_public.HomePageView.as_view(), name='public_home'),
    path('', include('home.urls_public', namespace='home')),
    path('admin/', admin.site.urls),
    path('users/', include('allauth.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('blogs/', include('blogs.urls_public', namespace='blogs_public')),
    path('builder/', include('resumes.urls', namespace='resume')),
    path('tinymce/upload/', HandleEditorUpload.as_view()),
    path('b/', include('blogs.urls', namespace='blogs'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
