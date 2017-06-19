from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

import views


urlpatterns = [
    #root
    url(r'^$', views.api_root, name='api_root'),

    #functions
    url(r'^add/?$', views.add, name='add'),
    url(r'^hello_world/$', views.hello_world, name='hello_world'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
