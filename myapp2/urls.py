from django.urls import path 
from . import views 
from django.conf.urls.static import static
from django.conf import settings
  
urlpatterns = [ 
    path('', views.snippet_detail_view), 
    path('thanks/', views.thanks)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)