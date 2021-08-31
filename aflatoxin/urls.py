from django.urls import path
from . import views

'''
Author: Dhanasekaran K
'''

urlpatterns = [
    path('test', views.Testfunction.as_view(), name='test'),
    path('test/<str:id>', views.Testfunction.as_view(), name='test'),
    path('crop_list', views.AflatoxinCropList.as_view(), name='crop_list'),
    path('toxin_list', views.ToxinList.as_view(), name='toxin_list'),
    path('toxin_list/<str:id>', views.ToxinList.as_view(), name='toxin_list')
]