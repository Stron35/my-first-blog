from django.urls import path
from .views import *

urlpatterns = [
	path('',post_list, name='post_list'),
	path('post/new/', PostCreate.as_view(), name='post_create'),
	path('post/<str:slug>/', post_detail, name='post_detail'),
	path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'), 
	path('post/<str:slug>/edit/', PostEdit.as_view(), name='post_edit'),
	]