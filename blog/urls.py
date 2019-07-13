from django.urls import path
from .views import *

urlpatterns = [
	path('',post_list, name='post_list'),
	path('post/new/', PostCreate.as_view(), name='post_create'),
	#path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<str:slug>/', post_detail, name='post_detail'),
	path('post/<str:slug>/edit/', post_edit, name='post_edit'),
	]