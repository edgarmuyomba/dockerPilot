from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:user_id>/', views.edit, name='edit'),
    path('new_user/', views.new_user, name='new_user'),
    path('list/', views.list, name='list'),
]