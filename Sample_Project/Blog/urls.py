from django.urls import path
from . import views # should be inside app folder

urlpatterns = [#included the views and
    path('', views.home, name='Blog-Home'),
    path('about/', views.about, name='Blog-about'),
]