from django.urls import path
from auth_app import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('register/', views.register, name='register')
]
