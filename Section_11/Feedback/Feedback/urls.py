"""
URL configuration for Feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('profiles/', include('profiles.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Because of securitiy reason to not render all thing on browser (insted of static folder of app) need to aware Django for that  
# When we render file/image folder and to serving we need to aware django so with adding MEDIA_URL in setting.py file alongside with + static() we aware here as well.
# static take two argument 1.The URL which shold be use to exposing file 2.Path on file system then exposing acctual file.


