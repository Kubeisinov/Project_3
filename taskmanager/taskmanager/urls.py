from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainer.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
