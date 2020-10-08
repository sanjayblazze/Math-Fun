from django.contrib import admin
from django.urls import path, include
from MathsFun import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Standard, name='home-page'),
    path('MathsFun/', include('MathsFun.urls')),
    path('registration/', include('allauth.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
