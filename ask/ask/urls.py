from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'test'),
    # url(r'^login/', 'test'),
    # url(r'^signup/', 'test'),
    #url(r'^question/\d+/', 'test'),
    # url(r'^ask/', 'test'),
    #url(r'^popular/', 'test'),
    # url(r'^new/', 'test'), 
    url(r'^$', views.get_page, name='get_page'),
    url(r'^popular/$', views.get_popular, name='get_popular'),
    url(r'^question/(?P<question_id>\d+)/$', views.get_question, name='get_question'),
    url(r'^admin/', include(admin.site.urls)),
]
