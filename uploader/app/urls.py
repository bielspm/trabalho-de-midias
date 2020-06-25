"""
Define padrões de URL para users
"""

from django.urls import path
from app.views import home, store, edit, delete, index, show

urlpatterns = [
    path('', home, name='main'),
    path('upload/store/', store, name='store'),
    path('upload/edit/<int:upload_id>/', edit, name='edit'),
    path('upload/delete/<int:upload_id>/', delete, name='delete'),
    path('upload/index/', index, name='index'),
    path('upload/<int:upload_id>/show/', show, name='show'),

] 