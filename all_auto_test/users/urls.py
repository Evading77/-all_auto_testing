from django.urls import path

from users.views import LoginView

urlpatterns=[
    #登录的路由
    path('login/',LoginView.as_view(),name='login'),
]