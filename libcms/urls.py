# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.admin.sites import site
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^', include('index.urls', namespace='index')),
    (r'^core/', include('core.urls', namespace='core')),
    (r'^accounts/', include('accounts.urls', namespace='accounts')),
    (r'^profile/', include('profile.urls', namespace='profile')),
    (r'^filebrowser/', include('filebrowser.urls', namespace='filebrowser')),
    (r'^menu/', include('menu.urls', namespace='menu')),
    (r'^pages/', include('pages.urls', namespace='pages')),
    (r'^news/', include('news.urls', namespace='news')),
    (r'^events/', include('events.urls', namespace='events')),
    (r'^statistics/', include('statistics.urls', namespace='statistics')),
    # (r'^participants/(?P<library_id>\d+)/pages/', include('participants_pages.urls', namespace='participants_pages')),
    (r'^participants/', include('participants.urls', namespace='participants')),
    # (r'^professionals/pages/', include('professionals_pages.urls', namespace='professionals_pages')),
    # (r'^professionals/news/', include('professionals_news.urls', namespace='professionals_news')),
    # (r'^professionals/', include('professionals.urls', namespace='professionals')),
    (r'^polls/', include('polls.urls', namespace='polls')),
    (r'^personal/', include('personal.urls', namespace='personal')),
    (r'^ask_librarian/', include('ask_librarian.urls', namespace='ask_librarian')),
    (r'^ssearch/', include('ssearch.urls', namespace='ssearch')),
    (r'^dl/', include('rbooks.urls', namespace='rbooks')),
    (r'^orders/', include('orders.urls', namespace='orders')),
    (r'^rorders/', include('ruslan_cabinet.urls', namespace='ruslan_cabinet')),
    (r'^extorders/', include('external_orders.urls', namespace='external_orders')),
    (r'^urt/', include('urt.urls', namespace='urt')),
    (r'^mydocs/', include('mydocs.urls', namespace='mydocs')),
    (r'^zgate/', include('zgate.urls')),
    (r'^forum/', include('forum.urls', namespace='forum')),
    (r'^guestbook/', include('guestbook.urls', namespace='guestbook')),
    (r'^newinlib/', include('newinlib.urls', namespace='newinlib')),
    (r'^attacher/', include('attacher.urls', namespace='attacher')),
    (r'^esia_sso/', include('sso_esia.urls', namespace='sso_esia')),
    (r'^sso_ruslan/', include('sso_ruslan.urls', namespace='sso_ruslan')),
    (r'^tatedu_sso/', include('sso_tatedu.urls', namespace='sso_tatedu')),
    (r'^participants/news/', include('participant_news.all_frontend.urls', namespace='participant_all_news')),
    (r'^rr/', include('recommended_reading.urls', namespace='recommended_reading')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/news/', include('participant_news.urls', namespace='participant_news')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/pages/',
     include('participant_pages.urls', namespace='participant_pages')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/events/',
     include('participant_events.urls', namespace='participant_events')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/photopolls/',
     include('participant_photopolls.urls', namespace='participant_photopolls')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/menu/', include('participant_menu.urls', namespace='participant_menu')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/banners/',
     include('participant_banners.urls', namespace='participant_banners')),
    (r'^site/(?P<library_code>[_\-0-9A-Za-z]+)/', include('participant_site.urls', namespace='participant_site')),

    #    (r'^mydocs/', include('mydocs.urls',)),
    # Uncomment the next line to enable the admin:
    url(r'^radmin/', include(admin.site.urls)),
    url(r'^jsi18n/$', site.i18n_javascript, name='jsi18n'),
    #url(r'^sauth/', include('social_auth.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
