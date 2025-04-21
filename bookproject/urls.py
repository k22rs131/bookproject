from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health_check_view(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('book.urls')),
    path("", health_check_view),  # これを追加
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)