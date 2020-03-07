from .views import ShowList,ShowDetailList,UserDetailList
from django.conf.urls import url
from django.contrib import admin

urlpatterns=[
		url(r'^$',ShowList.as_view(),name='Show_list'),
		url(r'Search/$',ShowDetailList.as_view(),name='Show_detail'),
		url(r'^Auth/',UserDetailList.as_view(),name='UserDetails'),
		url(r'^Distributors/$',DistributorList.as_view(),name='Distributor_list'),
		#url(r'^(?P<title>[\w-]+)/edit/$',BlogUpdateList.as_view(),name='blod_detail'),
]