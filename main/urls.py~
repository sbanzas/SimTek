from django.conf.urls import patterns, include, url
from main.views import user_views

urlpatterns = patterns('',
    # INDEX URL PATTERNS
    url(r'^$', user_views.index_view, name='index'),
    # AUTHENTICATION URL PATTERNS
    url(r'^login/$', user_views.login_view, name='login'),
    url(r'^logout/$', user_views.logout_view, name='logout'),
    url(r'^register/$', user_views.registration_view, name='register'),
    url(r'^dashboard/$', user_views.home_page_view, name='dashboard'),
)
