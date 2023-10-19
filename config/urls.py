from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('', include('user.urls')),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
