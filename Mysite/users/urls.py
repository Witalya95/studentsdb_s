from django.conf.urls import url
from django.contrib.auth.views import login


from . import views


urlpatterns = [

	# Сторінка входу

	url(r'^login/$', login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_views, name='logout'),
    url(r'^register/$', views.register, name='register'),



]