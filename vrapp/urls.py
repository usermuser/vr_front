
from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.ProcessListView.as_view(), name='process_list'),
=======
    url(r'^$', views.index, name='index'),
>>>>>>> e5ab72fa5fc8bb8ed5d99ded23dfa8793c9622b0
#    url(r'^(?<>[0-9]+)/$', views.detail, name='detail'),
]
