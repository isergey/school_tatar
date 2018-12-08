# coding: utf-8
from django.conf.urls import *
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^org/$', views.org_stats, name='org_stats'),
    url(r'^search/$', views.search_stats, name='search_stats'),
    url(r'^users_at_mini_sites/$', views.users_at_mini_sites, name='users_at_mini_sites'),
    url(r'^orgs_statistic/$', views.orgs_statistic, name='orgs_statistic'),
    url(r'^org_statistic/$', views.org_statistic, name='org_statistic'),
    url(r'^portal_statistic/$', views.portal_statistic, name='portal_statistic'),
    url(r'^watch/$', views.watch, name='watch'),
)
