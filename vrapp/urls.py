
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProcessListView.as_view(), name='process_list'),
#    url(r'^(?<>[0-9]+)/$', views.detail, name='detail'),
]
