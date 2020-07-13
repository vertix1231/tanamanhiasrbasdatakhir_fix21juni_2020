from django.conf.urls import url

from . import views

urlpatterns = [
    #Leave as empty string for base url
    url(r'^delete/(?P<delete_id>[0-9]+)$', views.deletePost, name='delete'),
    url(r'^update/(?P<update_id>[0-9]+)$', views.updatePost, name='update'),
	url(r'^singlepost/(?P<slugInput>[\w-]+)/$', views.detailPost, name='single'),
	url(r'^manage/create/$', views.createPost, name='create'),
	url(r'^manage/$', views.managePost, name='manage'),
	url(r'^$', views.allPost ,name="allpost"),
	]