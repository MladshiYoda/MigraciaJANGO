from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('how-to-find/', views.how_to_find, name='how_to_find'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]