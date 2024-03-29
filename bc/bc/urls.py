from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', include('cv.urls')),
    path('admin/', admin.site.urls),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
