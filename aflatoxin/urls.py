from django.urls import path
from . import views

'''
Author: Dhanasekaran K
'''

urlpatterns = [
    path('test', views.Testfunction.as_view(), name='test'),
    path('test/<str:id>', views.Testfunction.as_view(), name='test')
]