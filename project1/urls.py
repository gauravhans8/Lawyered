from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    url(r'^lawyered/', include('lawyered.urls')),
#    url(r'^ath/', include('laath.urls')),
	url(r'^login/$', views.login, {'template_name' : 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)