from django.urls import path
from profile_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('profile_page/', views.PP, name='pp')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
