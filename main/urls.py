from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = ([
                  path('admin/', admin.site.urls),
                  path('',include('blog.urls'))
              ] + static(settings.STATIC_URL, documect_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           documect_root=settings.MEDIA_ROOT))
