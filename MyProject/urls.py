from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyProjectApp.urls')),
    path('', include('Register.urls')),
    path('', include('Contact.urls')),
    path('', include('Shop.urls')),
]

handler404 = 'MyProjectApp.views.handler404'
handler500 = 'MyProjectApp.views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)