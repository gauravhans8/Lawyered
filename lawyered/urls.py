
from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import logout
from . import views
app_name = 'lawyered'
urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^login/$', views.login, {'template_name' : 'login.html'}),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/$',login, name = 'login'),
	url(r'^logout/$',logout, {'next_page': '/lawyered'}, name='logout'),
	url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
	url(r'^search/$', views.person_list, name='search'), 
	url(r'^divorce/$', views.divorce, name='divorce'),

]
#url(r'^$', views.dashboard, name='dashboard'),url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),url(r'^login/$', views.user_login,name='login'),
