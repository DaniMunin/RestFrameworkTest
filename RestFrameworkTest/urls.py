from django.conf.urls import patterns, include, url
from ProposalVoting import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'ProposalVoting.views',
    url(r'^proposal$', 'proposal_list'),
    url(r'^proposals/(?P<pk>[0-9]+)$', 'proposal_detail'),
    url(r'^users/(?P<pk>[0-9]+)$',views.user_detail.as_view()),
    url(r'^users$',views.user_list.as_view()), url(r'^proposal$', 'proposal_list'),
    url(r'^proposal/$', 'proposal_list'),
    url(r'^proposals/(?P<pk>[0-9]+)/$', 'proposal_detail'),
    url(r'^users/(?P<pk>[0-9]+)/$',views.user_detail.as_view()),
    url(r'^users/$',views.user_list.as_view()),

    # Examples:
    # url(r'^$', 'RestFrameworkTest.views.home', name='home'),
    # url(r'^RestFrameworkTest/', include('RestFrameworkTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
