from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:question_id>', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]