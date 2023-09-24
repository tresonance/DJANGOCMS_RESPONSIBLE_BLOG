"""my_blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('cms.urls')),
    re_path(r'^select2/', include('django_select2.urls')),  #for intenal link, see 'django-select2', in INSTALLED_APPLICAION inside sttings.py
    # re_path(r'^', include('djangocms_forms.urls')), # for djangocms form plugin, we comment becaus we have rrors while importing dangocms-forms inside INSTALLED_APPLICATIONS and requirements.txt
    re_path(r'^my_blog_app/', include(('my_blog_app.urls', 'my_blog_app'),  namespace='my_blog_app')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
