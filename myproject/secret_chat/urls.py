from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.generator, name='generator'),
    re_path(r'chat/(?P<link_slug>[\w-]+)/$',views.chat_begins,name='chat_begins'),
    re_path(r'save/', views.save_chat, name='save_chat'),
    re_path(r'read/', views.read_chat, name='read_chat'),
]