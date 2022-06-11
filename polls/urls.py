from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.index, name='index'),
  path('submit', views.submit_order, name='submit_order'),
  path('login', views.login, name='login'),
  path('confirm', views.confirm, name='confirm'),
  path('detail', views.detail, name='detail'),
]