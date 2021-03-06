from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HumanAPIView.as_view()),
    path('movies', MovieAPIView.as_view()),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
