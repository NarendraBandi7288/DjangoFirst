from django.conf.urls import url
from nariApp import views

urlpatterns = [
    url(r'^register/', views.studentRegisterView),
    url(r'^kitkat/', views.kitkatty),
    url(r'cook/', views.cook),
    url(r'horlicks/', views.horlicks),
    url(r'session/', views.session),
]
