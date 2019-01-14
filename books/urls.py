from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name='books'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'search/', views.book_search),
    url(r'^detail/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='detail'),
    url(r'^api/$', views.api_list),
    url(r'^api/(\d+)/$', views.api_detail),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    url(r'^authors/api/$', views.author_api_list),
    url(r'^authors/api/(\w+)/$', views.author_api_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)